from unittest import TestCase
from selenium import webdriver
from pages.signin_page import SigninPage

class test_Signin_Modal_Test(TestCase):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    baseUrl = "https://www.momondo.com/"
    driver.maximize_window()
    driver.get(baseUrl)
    smp = SigninPage(driver)

    def test_SigninModal(self):
        self.smp.clickHeatherSignin()
        self.smp.clickBooking()
        self.smp.checkBookingModal()

        # self.smp.clickSigninWithEmail()
        # self.smp.checkSigninWithEmail()
