from Additional.Browsers.ChromeBrowser import ChromeBrowser
from selenium.webdriver.common.by import By


class HomePageLocator:

    pictureBelowUniqueAndClean = "#post-9 > div > div:nth-child(1) > div > p:nth-child(1) > a > img"
    pictureBelowCustomerSupport = "#post-9 > div > div:nth-child(2) > div > p:nth-child(1) > i > a > img"
    pictureBelowVeryFlexible = "#post-9 > div > div:nth-child(3) > div > i > a > img"
    tab1Button = "a#ui-id-1"
    content1Title = "#tabs-1 > b"
    tab2Button = "a#ui-id-2"
    content2Title = "#tabs-2 > b"
    tab3Button = "a#ui-id-3"
    content3Title = "#tabs-3 > b"
    tab4Button = "a#ui-id-4"
    content4Title = "#tabs-4 > b"
    tab5Button = "a#ui-id-5"
    content5Title = "#tabs-5 > b"


class HomePage(ChromeBrowser):

    def open_demo_qa(self):
        self.driver.get("http://demoqa.com/")

    def click_picture_below_unique_and_clean(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.pictureBelowUniqueAndClean).click()

    def click_picture_below_customer_support(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.pictureBelowCustomerSupport).click()

    def click_picture_below_very_flexible(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.pictureBelowVeryFlexible).click()

    def click_tab1_button(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.tab1Button).click()

    def click_tab2_button(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.tab2Button).click()

    def click_tab3_button(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.tab3Button).click()

    def click_tab4_button(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.tab4Button).click()

    def click_tab5_button(self):
        self.driver.find_element(By.CSS_SELECTOR, HomePageLocator.tab5Button).click()
