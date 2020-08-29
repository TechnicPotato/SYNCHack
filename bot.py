import requests
import time
import getpass
import selenium
import sys
import csv
import opportunity

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options 
from bs4 import BeautifulSoup

class bot:
    """
    The bot class contains many of the necessary functions in order to navigate and scrape the website.

    Params
    -------
    website : str
        The site in which we need to scrape in question
    opportunity : 
    """
    def __init__(self, website, opportunity_type=None, field=None, headless=False):
        self.opportunity = opportunity_type
        self.field = field

        if headless:
            options = Options()
            options.headless = True

        # Initialisation
        self.website = website
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(website)
        
        # Store the page number
        self.page_no = 0


    def default_search(self):
        selector = "//select[@name='{type}']/option[text()='{text}']"
        if self.opportunity != None:
            self.driver.find_element_by_xpath(selector.format(type="opportunity_types",text=self.opportunity)).click()
        if self.field != None:
            self.driver.find_element_by_xpath(selector.format(type="opportunity_types",text=self.opportunity)).click()
        search = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div/form/fieldset/div/button/span")
        search.click()
        # Search always leads to initial page
        self.page_no = 1

    def scrape_page(self):
        """ Scrapes a page and retrurns a list of opportunities on the page"""
        # Wait time to allow for website to load.
        time.sleep(3)
        output = []
        # Find how many opportunities exist
        opportunities = (self.driver.find_elements_by_xpath("//div[@class='Boxstyle__Box-sc-1jxggr3-0 Teaserstyle__Teaser-egwky8-0 OpportunityTeaserstyle__OpportunityListing-sc-1vbfrdq-0 cqpUPt']"))
        
        # Confirmation checking
        for i in opportunities:
            rawstring = i.get_attribute('innerHTML')
            self.cleanstring(rawstring)
        return output
    
    def next_page(self):
        """Navigates to the next page within a search. Returns None if no further pages are found"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            selector = "li.pagination-item:nth-child({pageno}) > a:nth-child(1)".format(pageno = self.page_no) 
            # Sleep to allow page load
            time.sleep(3)
            link = self.driver.find_element_by_link_text(str(self.page_no + 1))
            link.click()
        except:
            return None
        return True

    def cleanstring(self, string):
        """From an innerHTML string, extract useful data and return an opportunity object"""
        soup = BeautifulSoup(string, "lxml")
        company, o_type = soup.find_all("p")
        info = soup.find("h2").text
        info_link = None
        app_link = None
        for i in soup.find_all("a", href=True):
            if i.text == "Apply now":
                app_link = i['href']
            elif i.text == info:
                info_link = self.website + i['href']

        rating =  soup.find("div", {"class":"rating__score"})
        review_link = None
        if rating != None:
            # Safe to be able to convert this to a usable format
            rating = rating.text
            for i in soup.find_all("a", href=True):
                if i.text.startswith("Read reviews"):
                    link = i['href']
            review_link = self.website + link
        
        output = opportunity(company.text, o_type.text, info, info_link, app=app_link)
        output.review_score(rating, review_link)
        return output

