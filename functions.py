import time
import getpass
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selectors import *

file_download_path = Path("C:/Users/"+getpass.getuser()+"/Downloads/")
main_page_the_internet_herokuapp = 'https://the-internet.herokuapp.com'

class Common():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_click(self, target, wait_time=30, selector_type=By.XPATH):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((selector_type, target)))
        self.driver.find_element_by_xpath(target).click()

class Actions(Common):

    def download_file(self):
        self.driver.get(main_page_the_internet_herokuapp)
        self.wait_click(file_download_page)
        self.wait_click(file_to_download)

    def does_file_exist(self):
        seconds_waited = 0
        while seconds_waited < 60 and Path.exists(file_download_path / self.driver.find_element_by_xpath(file_to_download).get_attribute('innerText')) == False:
            time.sleep(1)
            seconds_waited += 1
        if Path.exists(file_download_path / self.driver.find_element_by_xpath(file_to_download).get_attribute('innerText')):
            return True
        else:
            return False

    def search_for_typo_page_go_to(self):
        self.driver.get(main_page_the_internet_herokuapp)
        self.wait_click(typo_page)