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

class bot:
    """
    The bot class contains many of the necessary functions in order to navigate and scrape the website.

    Params
    -------
    website : str
        The site in which we need to scrape in question
    opportunity : 
    """
    def __init__(self, website, opportunity_type=None, field=None):
        self.opportunity = opportunity_type
        self.field = field

        # Initialisation
        self.driver = webdriver.Firefox()
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
        output = []
        
        return output
    
    def next_page(self):
        """Navigates to the next page within a search. Returns None if no further pages are found"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        selector = "li.pagination-item:nth-child({pageno}) > a:nth-child(1)".format(pageno = self.page_no)
        time.sleep(3)
        link = self.driver.find_element_by_link_text(str(self.page_no + 1))
        link.click()

