import unittest
from tests.test_navigation import NavigationTests
from tests.test_search import SearchFunction_Tests


# Get all tests from the test clases and run them
tc1 = unittest.TestLoader().loadTestsFromTestCase(NavigationTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SearchFunction_Tests)

# if tc1 or tc2 == TypeError:
#     tc1 = unittest.TestLoader().loadTestsFromTestCase(NavigationTests)
#     tc2 = unittest.TestLoader().loadTestsFromTestCase(SearchFunction_Tests)
# else:
