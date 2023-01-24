from unittest import TestCase
from selenium import webdriver
from pages.signin_page import SigninPage

class Signin_Page_Test(TestCase):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    baseUrl = "https://www.momondo.com/"
    driver.maximize_window()
    driver.get(baseUrl)
    sp = SigninPage(driver)

    def test_SigninModal(self):
        self.sp.clickHeatherSignin()
        self.sp.clickBooking()
        print(self.sp.checkBookingModal())
        # self.sp.clickFacebook()
        # assert self.sp.checkFbModal() is not None
        # self.sp.clickSigninWithEmail()
        # siginWithEmailResult = self.sp.checkSigninWithEmail()
        # self.sp.clickBooking()
        # bookingModalResult = self.sp.checkBookingModal()
        # self.sp.clickSigninWithEmail()
        # siginWithEmailResult = self.sp.checkSigninWithEmail()

        # assert siginWithEmailResult and fbModalResult and bookingModalResult is not None


