from unittest import TestCase
from pages.search_page import SearchPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SearchFunction_Tests(TestCase):
    chrom_opt = Options()
    chrom_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrom_opt)
    driver.implicitly_wait(5)
    baseUrl = "https://www.momondo.com/"
    driver.maximize_window()
    driver.get(baseUrl)
    sp = SearchPage(driver)

    def test_SearchFunction(self):
        from_destination = "San Francisco"         # enter correct name of the destinations!
        to_destination = "Tokyo"
        self.sp.clearFromInputField()
        self.sp.enterFromLocation(from_destination)
        self.sp.clickFromSuggestion(from_destination)
        self.sp.enterToLocation(to_destination)
        self.sp.clickToSuggestion(to_destination)
        self.sp.selectDepartureDate()
        self.sp.selectReturnDate()
        self.sp.clickSearch()
        search_location_result = self.sp.verifySearchResult(from_destination, to_destination)
        search_departure_date_result = self.sp.verifyDepartureDates()
        search_return_date_result = self.sp.verifyReturnDates()
        self.sp.scrollToPriceFilter()
        self.sp.clickPriceFilter()
        self.sp.usePriceSlider()
        search_price_filter = self.sp.verifyPriceFilterResult()
        print("\nsearch_location_result result is: " + str(search_location_result))
        print("search_date_resultD result is: " + str(search_departure_date_result))
        print("search_date_resultR result is: " + str(search_return_date_result))
        print("search_price_filter result is: " + str(search_price_filter))

        assert search_location_result
        assert search_departure_date_result
        assert search_return_date_result
        assert search_price_filter

        # assert search_location_result and search_date_result and search_price_filter
        # self.driver.quit()

