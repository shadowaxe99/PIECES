```python
import unittest
from selenium import webdriver

class FrontendTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_user_profile_form(self):
        self.driver.get('http://localhost:3000')
        user_profile_form = self.driver.find_element_by_id('userProfileForm')
        self.assertIsNotNone(user_profile_form)

    def test_recommendation_list(self):
        self.driver.get('http://localhost:3000')
        recommendation_list = self.driver.find_element_by_id('recommendationList')
        self.assertIsNotNone(recommendation_list)

    def test_search_form(self):
        self.driver.get('http://localhost:3000')
        search_form = self.driver.find_element_by_id('searchForm')
        self.assertIsNotNone(search_form)

    def test_itinerary_planner(self):
        self.driver.get('http://localhost:3000')
        itinerary_planner = self.driver.find_element_by_id('itineraryPlanner')
        self.assertIsNotNone(itinerary_planner)

    def test_alert_box(self):
        self.driver.get('http://localhost:3000')
        alert_box = self.driver.find_element_by_id('alertBox')
        self.assertIsNotNone(alert_box)

    def test_booking_form(self):
        self.driver.get('http://localhost:3000')
        booking_form = self.driver.find_element_by_id('bookingForm')
        self.assertIsNotNone(booking_form)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```