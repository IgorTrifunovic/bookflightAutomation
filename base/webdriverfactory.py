"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        driver = webdriver.Chrome('/home/igor/chromedriver')
        driver.implicitly_wait(3)
        baseurl = "https://www.momondo.com/"
        driver.get(baseurl)
        driver.maximize_window()
        return driver



        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        # baseURL = "https://www.momondo.com/"
        # if self.browser == "iexplorer":
        #     # Set ie driver
        #     driver = webdriver.Ie()
        # elif self.browser == "firefox":
        #     driver = webdriver.Firefox()
        # elif self.browser == "chrome":
        #     # Set chrome driver
        #     driver = webdriver.Chrome()
        # else:
        #     driver = webdriver.Chrome()
        # # Setting Driver Implicit Time out for An Element
        # driver.implicitly_wait(10)
        # # Maximize the window
        # driver.maximize_window()
        # # Loading browser with App URL
        # driver.get(baseURL)
        # # driver.add_cookie({""})
        # # driver.add_cookie({""})
        # return driver