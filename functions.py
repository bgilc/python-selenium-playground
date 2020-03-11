from selenium import webdriver

class Common():

    def __init__(self):
        self.driver = webdriver.Chrome()

class Actions(Common):
    pass