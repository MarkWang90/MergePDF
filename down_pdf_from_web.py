# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:38:37 2018

@author: markp
"""

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import time
import glob
import shutil

class TWDB_Scraper(object):
    def __init__(self,weblink):
        self.url = weblink
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.delay = 3 # of seconds to wait
        
    def load_page(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_all_elements_located((By.ID,"headID")))
            print("page is ready")
        except TimeoutException:
            print("loading took too much time") 