import time
import getpass
import keyboard
import requests
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from selectors import *

file_download_path = Path("C:/Users/" + getpass.getuser() + "/Downloads/")
file_to_upload = Path("C:/Users/" + getpass.getuser() + "/test_file.jpg")


class Common():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_click(self, target, wait_time=30, selector_type=By.XPATH):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((selector_type, target)))
        self.driver.find_element(By.XPATH, target).click()

    def search_for_click(self, value):
        searching = f"//*[text() = '{value}']"
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, searching)))
        self.driver.find_element(By.XPATH, searching).click()

    def does_element_exist(self, selector):
        if len(selector) > 0:
            return True
        else:
            return False


class Actions(Common):

    def ab(self):
        self.search_for_click('A/B Testing')
        text_value_before_cookie_insert = self.driver.find_element(By.TAG_NAME, 'h3').text
        self.driver.add_cookie({"name": "optimizelyOptOut", "value": "true"})
        self.driver.refresh()
        text_value_after_cookie_insert = self.driver.find_element(By.TAG_NAME, 'h3').text
        if text_value_before_cookie_insert == 'A/B Test Control' or text_value_before_cookie_insert == 'A/B Test Variation 1':
            before_cookie = True
        else:
            before_cookie = False
        if text_value_after_cookie_insert == 'No A/B Test':
            after_cookie = True
        else:
            after_cookie = False
        if before_cookie == True and after_cookie == True:
            return True
        else:
            return False

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

    def broken_images(self):
        self.search_for_click('Broken Images')
        image1 = requests.get('https://the-internet.herokuapp.com/asdf.jpg').status_code
        image2 = requests.get('https://the-internet.herokuapp.com/hjkl.jpg').status_code
        image3 = requests.get('https://the-internet.herokuapp.com/img/avatar-blank.jpg').status_code
        if image1 == 404 and image2 == 404 and image3 == 200:
            return True
        else:
            return False

    def checkboxes(self):
        self.search_for_click('Checkboxes')
        self.wait_click(checkboxes_input1)
        self.wait_click(checkboxes_input2)

    def context_menu(self):
        self.search_for_click('Context Menu')
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(By.ID, 'hot-spot')).perform()
        EC.alert_is_present()
        self.driver.switch_to.alert.dismiss()
        try:
            self.driver.switch_to.alert.dismiss()
        except NoAlertPresentException:
            return True

    def download_file(self):
        self.search_for_click('File Download')
        self.wait_click(file_to_download)

    def does_file_exist(self):
        seconds_waited = 0
        while seconds_waited < 60 and Path.exists(
                file_download_path / self.driver.find_element(By.XPATH, file_to_download).get_attribute(
                    'innerText')) == False:
            time.sleep(1)
            seconds_waited += 1
        if Path.exists(
                file_download_path / self.driver.find_element(By.XPATH, file_to_download).get_attribute('innerText')):
            return True
        else:
            return False

    def forgot_password(self):
        self.search_for_click('Forgot Password')
        self.driver.find_element(By.XPATH, forgot_password_input_field).send_keys('xkscd@cksx.pl')
        self.driver.find_element(By.XPATH, forgot_password_button).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, forgot_password_confirmation)))

    def search_for_typo_page_go_to(self):
        self.search_for_click('Typos')

    def upload_file(self):
        self.search_for_click('File Upload')
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, file_upload_input)))
        self.driver.find_element(By.XPATH, file_upload_input).send_keys(str(file_to_upload))
        self.driver.find_element(By.XPATH, file_upload_button).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, file_upload_result)))
