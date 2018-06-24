from selenium import webdriver


class ChromeBrowser:

    driver = webdriver.Chrome(r'C:\Users\Mariusz\IdeaProjects\PythonTestExercises3\Additional\Drivers\chromedriver.exe')
    driver.maximize_window()
    # driver.implicitly_wait(30)
    # driver.set_page_load_timeout(30)


    def close(context):
        context.driver.close()
