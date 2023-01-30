import time

from base.selenium_driver import SeleniumDriver
from selenium.webdriver import Remote


class SigninPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Locators
    _signInFromHeather = "div.sign-in-nav-link"
    _fbBtn = "button[aria-label='Continue with Facebook']"
    _bookingBtn = ".social-button-icon.social-button-icon-booking"
    _continueWithEmailBtn = "div.continueWithEmail"
    _bookingTitle = "a[rel='noopener noreferrer']"
    _fbTitle = "#homelink"
    _signinWithEmailVerifElement = 'input[aria-label="Email address"]'

    def clickHeatherSignin(self):
        self.elementClick(self._signInFromHeather, locatorType="css")
        time.sleep(3)

    def clickSigninWithEmail(self):
        self.elementClick(self._continueWithEmailBtn, locatorType="css")

    def clickFacebook(self):
        self.elementClick(self._fbBtn, locatorType="css")

    # def clickBooking(self):


    def checkSigninWithEmail(self):
        result = self.isElementPresent(self._signinWithEmailVerifElement)
        self.log.info("Found SignIn With Email Modal!")
        return result

    def checkBookingModal(self):
        booking_page = None

        remote = Remote(self.driver)
        self.elementClick(self._bookingBtn, locatorType="css")
        time.sleep(2)
        asd = remote.window_handles
        print(len(asd))
        remote.switch_to.new_window()
        time.sleep(2)
        asd = remote.window_handles
        print(len(asd))

        # remote.close()
        # remote.switch_to.window(remote.window_handles[0])
        # main_page = remote.current_window_handle
        # self.log.info(main_page)
        # self.elementClick(self._bookingBtn, locatorType="css")
        # remote.switch_to.window(remote.window_handles[0])
        # elem = self.getElement(self._bookingTitle, "css")
        # self.log.info(elem)
        # time.sleep(90000)
        #
        # return elem




        # time.sleep(1)
        # for handle in remote.window_handles:
        #     if handle != main_page:
        #         booking_page = handle
        #
        # remote.switch_to.window(booking_page)
        # self.log.info("booking handle is: " + booking_page)
        # return booking_page




        # self.log.info("=========entered check booking modal============")
        # remote = Remote(self.driver)
        #
        # if self.getElement(self._bookingTitle, "css") is None:
        #     self.log.info("Switching browser window!")
        #     for handle in remote.window_handles:
        #         self.log.info(handle)
        #         try:
        #             self.getElement(self._bookingTitle, "css")
        #             except:



            # oldHanlde = remote.window_handles[0]
            # self.log.info(oldHanlde)
            # newHanlde = remote.window_handles[1]
            # remote.switch_to.window(newHanlde)
            # self.log.info(newHanlde)
        #     result = self.getElement(self._bookingTitle)
        # else:
        #     self.log.info("Found Facebook Modal!")
        #     # self.closeWindow()
        # return result



        # result = self.isElementPresent(self._bookingTitle)
        # if result is None:
        #     self.switchToNewWindow()
        #     result = self.isElementPresent(self._bookingTitle)
        #     self.closeWindow()
        # else:
        #     self.switchToNewWindow()
        #
        #     self.log.info("Found Booking Modal!")
        # return result

    def checkFbModal(self):
        result = self.getElement(self._fbTitle)
        if result is None:
            self.switchToNewWindow()
            result = self.getElement(self._fbTitle)
        else:
            self.log.info("Found Facebook Modal!")
            # self.closeWindow()
        return result


