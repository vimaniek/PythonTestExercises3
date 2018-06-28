from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Selector(object):

    def __init__(self, ref, find_element_by=By.CSS_SELECTOR):
        self.ref = ref
        self.find_element_by = find_element_by

    def to_element(self):
        return self.find_element_by, self.ref


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def _click_element(self, selector: Selector):
        self.driver.find_element(*selector.to_element()).click()

    def _get_page(self, url):
        self.driver.get(url)

    def _send_keys(self, selector: Selector, text):
        self.driver.find_element(*selector.to_element()).clear()
        self.driver.find_element(*selector.to_element()).send_keys(text)

    def _set_dropdown_list(self, selector: Selector, value):
        # jest problem jeśli w value są stringi, ale w stringach są cyfry - trzeba to uwzględnić
        if str(value).isdigit():
            self.select = Select(self.driver.find_element(*selector.to_element())).select_by_index(value)
        else:
            self.select = Select(self.driver.find_element(*selector.to_element())).select_by_value(value)
