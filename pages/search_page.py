import time
from base.selenium_driver import SeleniumDriver
from datetime import datetime
from datetime import timedelta

class SearchPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Locators
# 1.CSS:
    _clearPastDestinations = "svg[class*='vvTc-item-icon']"
    _fromLocation_input = "input[placeholder='From?']"
    _toLocation_input = "input[placeholder='To?']"
    _searchBtn = "button[title='Search'] span"
    _priceField = "h3[id*='price-title-text']"
    _priceSliderHandle = "div[id*='price-price-slider-sliderWidget-handle-0']"
    _suggestionFromDestination = "#flight-origin-smarty-input-list > li:nth-child(1) > div > div.JyN0-name-container > div > span.JyN0-name"
    _suggestionToDestination = "#flight-destination-smarty-input-list > li:nth-child(1) > div > div.JyN0-name-container > div > span.JyN0-name"
    _suggestedAirports = "div.JyN0-sub > span > svg" # depricated
    _searchResult_from = "div[title*='{}']"   # this element is different from non webdriver browser!
    _departureDateDropdown = "div:nth-child(1) > span > span.sR_k-value"
    _returnDateDropdown = "div:nth-child(3) > span > span.sR_k-value"
    _dateElement = 'div[aria-label*="{}"]'
    _datePreviousMonthChangeBtn = 'button[aria-label="Previous month"]'
    _dateNextMonthChangeBtn = 'button[aria-label="Next Month"]'
    _searchResultDates = """button[class='Button-No-Standard-Style js-bar item selected '][data-date*="{}"]"""

# Inputs:
    def clearFromInputField(self):
        self.elementClick(self._clearPastDestinations)

    def clickFromSuggestion(self, from_destination):
        suggestion = self.getText(self._suggestionFromDestination)
        if from_destination in suggestion:
            self.elementClick(self._suggestionFromDestination)

    def clickToSuggestion(self, to_destination):
        suggestion = self.getText(self._suggestionToDestination)
        if to_destination in suggestion:
            self.elementClick(self._suggestionToDestination)

    def enterFromLocation(self, fromDestination):
        self.sendKeys(fromDestination, self._fromLocation_input)
        time.sleep(1)

    def enterToLocation(self, toLocation):
        self.sendKeys(toLocation, self._toLocation_input)
        time.sleep(1)

    def clickSearch(self):
        self.elementClick(self._searchBtn)
        time.sleep(2)

    def scrollToPriceFilter(self):
        self.webScroll("down")
        self.log.info("Scrolled down once")
        time.sleep(3)

        self.webScroll("down")
        self.log.info("Scrolled down twice")

        time.sleep(3)
        self.webScroll("down")
        self.log.info("Scrolled down third time")


    def clickPriceFilter(self):
        self.elementClick(self._priceField)

    def usePriceSlider(self):
        time.sleep(3)
        self.moveSlideBar(100, 0, self.getElement(self._priceSliderHandle))
        time.sleep(6)

    today = datetime.now().strftime("%A %B %-d")
    def selectDepartureDate(self):
        global today
        self.elementClick(self._departureDateDropdown)
        for x in range(0, 12):
            if self.isElementPresent(self._dateElement.format(today)) is False:
                if x in range(0, 1):
                    self.log.info("Return date not found, trying previous month!")
                    self.elementClick(self._datePreviousMonthChangeBtn)
                    if self.isElementPresent(self._dateElement.format(today)) is False:
                        self.log.info("Return date not found, trying next month!")
                        self.elementClick(self._dateNextMonthChangeBtn)
                else:
                    self.log.info("Return date not found, trying next month!")
                    self.elementClick(self._dateNextMonthChangeBtn)
            else:
                self.log.info("Return date is found, selecting it!")
                self.elementClick(self._dateElement.format(today))
                break


    returnDate = datetime.now() + timedelta(days=100)
    returnDateStr = returnDate.strftime("%A %B %-d")
    def selectReturnDate(self):
        global returnDate
        global returnDateStr
        self.elementClick(self._returnDateDropdown)
        for x in range(0, 12):
            if self.isElementPresent(self._dateElement.format(returnDateStr)) is False:
                if x in range(0, 1):
                    self.log.info("Return date not found, trying previous month!")
                    self.elementClick(self._datePreviousMonthChangeBtn)
                    if self.isElementPresent(self._dateElement.format(returnDateStr)) is False:
                        self.log.info("Return date not found, trying next month!")
                        self.elementClick(self._dateNextMonthChangeBtn)
                else:
                    self.log.info("Return date not found, trying next month!")
                    self.elementClick(self._dateNextMonthChangeBtn)
            else:
                self.log.info("Return date is found, selecting it!")
                self.elementClick(self._dateElement.format(returnDateStr))
                break

    def clickPriceFilter(self):
        self.elementClick(self._priceField, "css")

    def usePriceSlider(self):
        time.sleep(2)
        self.moveSlideBar(40, 0, self.getElement(self._priceSliderHandle, "css"))


# Assertion:
    def verifySearchResult(self, from_destination, to_destination):
        self.webScroll("down")
        textFromDestination = self.getAttributeTitle(self._searchResult_from.format(from_destination), "css")
        textToDestination = self.getAttributeTitle(self._searchResult_from.format(to_destination), "css")
        if from_destination in textFromDestination and to_destination in textToDestination:
            return True

    def verifySearchDates(self):
        fromDate = self.isElementPresent(self._searchResultDates.format(today), "css")
        toDate = self.isElementPresent(self._searchResultDates.format(returnDateStr), "css")
        if fromDate and toDate is not None:
            return True

