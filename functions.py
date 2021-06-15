import time
import getpass
import keyboard
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selectors import *

file_download_path = Path("C:/Users/"+getpass.getuser()+"/Downloads/")
file_to_upload = Path("C:/Users/"+getpass.getuser()+"/test_file.jpg")

class Common():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_click(self, target, wait_time=30, selector_type=By.XPATH):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((selector_type, target)))
        self.driver.find_element_by_xpath(target).click()

    def search_for_click(self, value):
        searching = f"//*[text() = '{value}']"
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, searching)))
        self.driver.find_element_by_xpath(searching).click()

class Actions(Common):

    def add_remove_element(self):
        self.search_for_click('Add/Remove Elements')
        self.search_for_click('Add Element')
        self.search_for_click('Delete')

    def basic_authentication(self):
        self.search_for_click('Basic Auth')
        keyboard.write("admin")
        keyboard.press_and_release("tab")
        keyboard.write("admin")
        keyboard.press_and_release("enter")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, basic_auth_success)))

    def download_file(self):
        self.search_for_click('File Download')
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

    def forgot_password(self):
        self.search_for_click('Forgot Password')
        self.driver.find_element_by_xpath(forgot_password_input_field).send_keys('xkscd@cksx.pl')
        self.driver.find_element_by_xpath(forgot_password_button).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, forgot_password_confirmation)))

    def search_for_typo_page_go_to(self):
        self.search_for_click('Typos')

    def upload_file(self):
        self.search_for_click('File Upload')
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, file_upload_input)))
        self.driver.find_element_by_xpath(file_upload_input).send_keys(str(file_to_upload))
        self.driver.find_element_by_xpath(file_upload_button).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, file_upload_result)))