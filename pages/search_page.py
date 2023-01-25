import time
from base.selenium_driver import SeleniumDriver
from datetime import datetime
from datetime import timedelta


todaySelect = datetime.now().strftime("%A %B %-d")
# todaySelect = "Wednesday May 10"      #test value
returnDate = datetime.now() + timedelta(days=100)
returnDateSelect = returnDate.strftime("%A %B %-d")
todayAssert = datetime.now().strftime("%Y" + "-" + "%m" + "-" + "%d")
returnDateAssert = returnDate.strftime("%Y" + "-" + "%m" + "-" + "%d")

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
    _priceField = "div[id*=price]"  #".price-section"        #"div[id*='price-title'] > div"      #"h3[id*='price-title-text']"
    _priceSliderHandle = "div[id*='price-price-slider-sliderWidget-handle-0']"
    _priceSliderRail = "div[id*=price-price-slider-sliderWidget] > div.header > div"
    _priceFilterMaxRange = "div[id*=price-price-slider-rangeLabel] > span.max"
    _pricesOnFlightsPage = "div[class*='price-text']"

    _suggestionFromDestination = "#flight-origin-smarty-input-list > li:nth-child(1) > div > div.JyN0-name-container > div > span.JyN0-name"
    _suggestionToDestination = "#flight-destination-smarty-input-list > li:nth-child(1) > div > div.JyN0-name-container > div > span.JyN0-name"
    _suggestedAirports = "div.JyN0-sub > span > svg"  # depricated
    _searchResult_from = "div[title*='{}']"   # this element is different from non webdriver browser!
    _departureDateDropdown = "div:nth-child(1) > span > span.sR_k-value"
    _returnDateDropdown = "div:nth-child(3) > span > span.sR_k-value"
    _dateElement = 'div[aria-label*="{}"]'
    _datePreviousMonthChangeBtn = 'button[aria-label="Previous month"]'
    _dateNextMonthChangeBtn = 'button[aria-label="Next Month"]'
    _searchResultDates = """button[class='Button-No-Standard-Style js-bar item selected '][data-date*="{}"]"""
    _priceFilterResultOnPage = "div[class*=price-text]"

    _roundTripDropdown = "select[aria-label='Trip type']"
    _travelersDropdown = "div.zcIg.zcIg-pres-inline > div:nth-child(2) > div"
    _whichclassDropdown = 'select[aria-label="Cabin Class"]'
    _bagsDropdown = "div.zcIg.zcIg-pres-inline > div:nth-child(4) > div"
    _roundTripDropdownAssert = "#roundtrip"
    _travelersDropdown = "//span[contains(.,'Children')]"       # XPATH !!!!
    _whichclassDropdown = 'li[aria-label="Business"]'
    _bagsDropdown = "//span[contains(.,'Checked bag')]"     # XPATH !!!!



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
        time.sleep(5)

    def scrollToPriceFilter(self):
        self.webScroll("down")
        self.log.info("=====Scrolled down once=====")
        time.sleep(1)

    def clickPriceFilter(self):
        self.elementClick(self._priceField, "css")

    def usePriceSlider(self):
        self.moveSlideBarLeft(self.getElement(self._priceSliderHandle, "css"),
                              self.getElement(self._priceSliderRail, "css"))
        time.sleep(2)

    def selectDepartureDate(self):
        # global today
        self.elementClick(self._departureDateDropdown)
        for x in range(0, 12):
            if self.isElementPresent(self._dateElement.format(todaySelect)) is False:
                if x in range(0, 1):
                    self.log.info("Return date not found, trying previous month!")
                    self.elementClick(self._datePreviousMonthChangeBtn)
                    if self.isElementPresent(self._dateElement.format(todaySelect)) is False:
                        self.log.info("Return date not found, trying next month!")
                        self.elementClick(self._dateNextMonthChangeBtn)
                else:
                    self.log.info("Return date not found, trying next month!")
                    self.elementClick(self._dateNextMonthChangeBtn)
            else:
                self.log.info("Return date is found, selecting it!")
                self.elementClick(self._dateElement.format(todaySelect))
                self.log.info("Return date clicked!")
                break

    def selectReturnDate(self):
        self.elementClick(self._returnDateDropdown)
        for x in range(0, 12):
            if self.isElementPresent(self._dateElement.format(returnDateSelect)) is False:
                self.log.info("Return date not found, trying next month!")
                self.elementClick(self._dateNextMonthChangeBtn)
            else:
                if self.isEnabled(self._dateElement.format(returnDateSelect)) is False:
                    self.log.info("Return date is Disabled, trying next month for enabled element match!")
                    self.elementClick(self._dateNextMonthChangeBtn)
                    time.sleep(1)

                else:
                    if self.isEnabled(self._dateElement.format(returnDateSelect)) is True:
                        self.elementClick(self._dateElement.format(returnDateSelect))
                        self.log.info("=== Return Date element found!!! ===")
                        break
                    else:
                        self.log.info("=== Return Date is still disabled, could not select it!!! ===")
                        break

            if self.isEnabled(self._dateElement.format(returnDateSelect)) is False:
                self.log.info("Return date is Disabled, trying next month for enabled element match!")
                self.elementClick(self._dateNextMonthChangeBtn)
                time.sleep(1)
            else:
                if self.isEnabled(self._dateElement.format(returnDateSelect)) is True:
                    self.elementClick(self._dateElement.format(returnDateSelect))
                    self.log.info("=== Return Date element found!!! ===")
                    break
                else:
                    self.log.info("=== Return Date is still disabled, could not select it!!! ===")
                    break





    # depricated (for removal)
        # for x in range(0, 12):
        #     if self.isEnabled(self._dateElement.format(returnDateSelect)) is False:
        #         self.log.info("Return date not found, trying next month!")
        #         self.elementClick(self._dateNextMonthChangeBtn)
        #     elif self.isEnabled(self._dateElement.format(returnDateSelect)) is True:
        #         time.sleep(1)
        #         self.elementClick(self._dateElement.format(returnDateSelect))
        #         self.log.info("=== Return Date element found!!! ===")
        #     else:
        #         self.log.info("=== Return Date is still disabled, could not select it!!! ===")
        #     self.elementClick(self._dateElement.format(returnDateSelect))
        #     time.sleep(1)
        #     break

    # Assertion:
    def verifySearchResult(self, from_destination, to_destination):
        textFromDestination = self.getAttributeTitle(self._searchResult_from.format(from_destination), "css")
        textToDestination = self.getAttributeTitle(self._searchResult_from.format(to_destination), "css")
        if from_destination in textFromDestination and to_destination in textToDestination:
            return True

    def verifyDepartureDates(self):
        element = self.isElementPresent(self._searchResultDates.format(todayAssert), "css")
        if element is True:
            self.log.info("Web Element with selected Departure date is present!")
            return True
        else:
            self.log.info("Web Element with selected Return date is NOT present! Changing results to False.")
            return False


    def verifyReturnDates(self):
        element = self.isElementPresent(self._searchResultDates.format(returnDateAssert), "css")
        if element is True:
            self.log.info("Web Element with selected Return date is present!")
            return True
        else:
            self.log.info("Web Element with selected Return date is NOT present! Changing results to False.")
            return False


    def priceListHandler(self, pricesAfterFilter):
        pricesTxts = []
        for eachPrice in pricesAfterFilter:
            if eachPrice is not None:
                one_price = eachPrice.text.strip('$').replace(',', '')
                pricesTxts.append(one_price)
            else:
                self.log.info("==== Prices after price filter are None!!! =====")
        return pricesTxts

    def verifyPriceFilterResult(self):
        priceText = self.getText(self._priceFilterMaxRange).strip('$').replace(',', '')
        priceInt = int(priceText)
        self.log.info("==== Filter should display flights up to this price: " + str(priceInt))
        pricesAfterFilter = self.getElementList(self._pricesOnFlightsPage, "css")

        pricesTxts = self.priceListHandler(pricesAfterFilter)
        pricesInts = []
        for eachPrice in pricesTxts:
            eachInt = int(eachPrice)
            pricesInts.append(eachInt)
            if any(x < priceInt for x in pricesInts):
                return True
            else:
                return False
        self.log.info("++++++Prices found on page are: ".join(str(pricesInts)))        # TEST it, -doesnt work,

            # result = any(map(lambda x: x < priceInt, pricesInts))
            # print(result)






