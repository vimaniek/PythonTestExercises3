from selenium import webdriver

from settings import CHROME_DRIVER


class ChromeBrowser:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.set_up_window()

    def set_up_window(self):
        self.driver.maximize_window()

    # driver.implicitly_wait(30)
    # driver.set_page_load_timeout(30)

    def close(self):
        self.driver.close()


class ChromeBrowserIphone(ChromeBrowser):

    def set_up_window(self):
        pass
