import unittest
from functions import *
from selectors import *

class TestCasesTheInternetHerokuapp(unittest.TestCase):

    def setUp(self):
        self.action = Actions()
        self.action.driver.get('https://the-internet.herokuapp.com')

    def tearDown(self):
        self.action.driver.quit()

    def test_add_remove_element(self):
        self.action.add_remove_element()
        self.assertEqual(False, self.action.does_element_exist(self.action.driver.find_elements_by_class_name('added-manually')), 'Button should not exist.')

    def test_basic_authentication(self):
        self.action.basic_authentication()
        self.assertEqual("Congratulations! You must have the proper credentials.",
                         self.action.driver.find_element_by_xpath(basic_auth_success).text,
                         'Auth failed')

    def test_download_file(self):
        self.action.download_file()
        self.assertTrue(self.action.does_file_exist())

    def test_forgot_password(self):
        self.action.forgot_password()
        self.assertEqual("Your e-mail's been sent!", self.action.driver.find_element_by_xpath(forgot_password_confirmation).text, "Something is wrong!")

    def test_search_for_typo(self):
        self.action.search_for_typo_page_go_to()
        self.assertEqual('This example demonstrates a typo being introduced. It does it randomly on each page load.', self.action.driver.find_element_by_xpath(text_to_check_first_line).get_attribute('outerText'), 'Typo detected!')
        self.assertEqual("Sometimes you'll see a typo, other times you won't.", self.action.driver.find_element_by_xpath(text_to_check_second_line).get_attribute('outerText'), 'Typo detected!')

    def test_file_upload(self):
        self.action.upload_file()
        self.assertEqual('test_file.jpg', self.action.driver.find_element_by_xpath(file_upload_result).get_attribute('innerText'), 'Upload failed!')

if __name__ == '__main__':
    unittest.main()