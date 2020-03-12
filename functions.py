import hashlib
import time
import os.path
from selenium import webdriver
from selectors import *

downloaded_file_hash = 'e2ad0e90d464b9ac9cb2854b34505d91a302249b152ff716e877933736ae0ab8212b97a831845586d7383bb2bbe60e09e29150099927445ce8c912285f900ed3'
main_page_the_internet_herokuapp = 'https://the-internet.herokuapp.com'

class Common():

    def __init__(self):
        self.driver = webdriver.Chrome()

class Actions(Common):

    def download_file(self):
        self.driver.get(main_page_the_internet_herokuapp)
        self.driver.find_element_by_xpath(file_download_page).click()
        self.driver.find_element_by_xpath(file_to_download).click()

    def downloaded_file_check_hash(self):
        with open(r'C:\Users\sion\Downloads\quality-assurance1.jpg', 'rb') as file_object:
            file = file_object.read()
        return hashlib.sha3_512(file).hexdigest()

    def does_file_exist(self):
        seconds_waited = 0
        while seconds_waited < 60 and os.path.isfile(r'C:\Users\sion\Downloads\quality-assurance1.jpg') == False:
            time.sleep(1)
            seconds_waited += 1

    def search_for_typo_page_go_to(self):
        self.driver.get(main_page_the_internet_herokuapp)
        self.driver.find_element_by_xpath(typo_page).click()