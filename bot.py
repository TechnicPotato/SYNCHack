import requests
import time
import getpass
import selenium
import sys
import csv

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

    def default_search(self):
        selector = "//select[@name='{type}']/option[text()='{text}']"
        if self.opportunity != None:
            self.driver.find_element_by_xpath(selector.format(type="opportunity_types",text=self.opportunity)).click()
        if self.field != None:
            self.driver.find_element_by_xpath(selector.format(type="opportunity_types",text=self.opportunity)).click()
        search = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div/form/fieldset/div/button/span")
        search.click()

            

