from Additional.Browsers.ChromeBrowser import ChromeBrowser
from selenium.webdriver.common.by import By


class Selector(object):

    def __init__(self, ref, find_element_by=By.CSS_SELECTOR):
        self.ref = ref
        self.find_element_by = find_element_by

    def to_element(self):
        return self.find_element_by, self.ref


class BasePage:
    def __init__(self):
        self.driver = ChromeBrowser().driver

    def _find_element_and_click(self, selector: Selector):
        self.driver.find_element(*selector.to_element()).click()
