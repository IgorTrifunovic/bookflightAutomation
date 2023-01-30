from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_Navigation():

    def test_navigation(self):
        baseUrl = "https://www.momondo.com/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        signInLink = driver.find_element(By.CSS_SELECTOR, "div.hsCY-menu-item-icon.hsCY-icon-with-badge")
        signInLink.click()


        flightLink = driver.find_element(By.CSS_SELECTOR, "[aria-label*='Search for flights']")
        webdriver.ActionChains(driver).move_to_element(flightLink).click(flightLink).perform()


        staysLink = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Search for hotels']")
        staysLink.click()


        carrentalLink = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Search for cars']")
        carrentalLink.click()

        # following click element method resulted in ElementClickInterceptedException
        # flightLink = driver.find_element(By.CSS_SELECTOR, "[aria-label*='Search for flights']")
        # flightLink.click()

        print("=-="*5 + " Test process finished with exit code Zero. " + "=-="*5)

tt = Test_Navigation()





