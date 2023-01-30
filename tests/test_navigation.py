from pages.navigation_page import NavigationPage
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class NavigationTests(unittest.TestCase):
    chrom_opt = Options()
    chrom_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrom_opt)
    driver.implicitly_wait(5)
    baseUrl = "https://www.momondo.com/"
    driver.maximize_window()
    driver.get(baseUrl)
    np = NavigationPage(driver)


    def test_Navigation_Menu(self):
        self.np.clickHeatherSignin()
        assert self.np.verifySignIn_page()

        self.np.clickSignIn()
        assert self.np.verifySignIn_page()

        self.np.clickFlightBtn()
        assert self.np.verifyFlights_page()

        self.np.clickStays()
        assert self.np.verifyStays_page()

        self.np.clickCarRental()
        assert self.np.verifyCarRental_page()

        self.np.clickCarTrainsBuses()
        assert self.np.verifyCarTrainBuses_page()

        self.np.clickPackages()
        assert self.np.verifyPackage_page()

        self.np.clickExplore()
        assert self.np.verifyExplore_page()

        self.np.clickTrips()
        assert self.np.verifyTrips_page()

        self.np.clickTravelRestrictions()
        assert self.np.verifyTravelRestrictions_page()
        # self.driver.quit()

