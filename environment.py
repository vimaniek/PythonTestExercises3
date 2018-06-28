from Additional.Browsers.ChromeBrowser import ChromeBrowser
from Pages.HomePage import HomePage
from Pages.MenuPage import MenuPage
from Pages.RegistrationPage import RegistrationPage
import time


def before_feature(context, feature):
    context.driver = ChromeBrowser().driver
    context.home = HomePage(context.driver)
    context.menu = MenuPage(context.driver)
    context.registration = RegistrationPage(context.driver)


def after_feature(context, feature):
    time.sleep(5)
    context.driver.close()

def before_step(context, step):
    time.sleep(0.5)


