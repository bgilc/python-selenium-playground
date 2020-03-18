import unittest
from functions import *
from selectors import *

class TestCasesTheInternetHerokuapp(unittest.TestCase):

    def setUp(self):
        self.action = Actions()

    def tearDown(self):
        self.action.driver.quit()

    def test_download_file(self):
        self.action.download_file()
        self.assertTrue(self.action.does_file_exist())

    def test_search_for_typo(self):
        self.action.search_for_typo_page_go_to()
        self.assertEqual('This example demonstrates a typo being introduced. It does it randomly on each page load.', self.action.driver.find_element_by_xpath(text_to_check_first_line).get_attribute('outerText'), 'Typo detected!')
        self.assertEqual("Sometimes you'll see a typo, other times you won't.", self.action.driver.find_element_by_xpath(text_to_check_second_line).get_attribute('outerText'), 'Typo detected!')

    def test_file_upload(self):
        self.action.upload_file()
        self.assertEqual('test_file.jpg', self.action.driver.find_element_by_xpath(file_upload_result).get_attribute('innerText'), 'Upload failed!')

if __name__ == '__main__':
    unittest.main()