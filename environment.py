from Additional.Browsers.ChromeBrowser import ChromeBrowser


def before_all(context):
    context.driver = ChromeBrowser()


def after_all(context):
    context.driver.close()
