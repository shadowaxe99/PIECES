```python
import unittest
from database.models import UserProfile, TravelRecommendation, SearchResult, Itinerary, Alert, BookingDetail
from database.queries import DatabaseQueries

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_queries = DatabaseQueries()

    def test_create_user_profile(self):
        user_profile = UserProfile('John Doe', 'johndoe@gmail.com', 'password123', 'Business', 'Delta', 'Hilton', 'First Class', 'Wi-Fi')
        self.db_queries.create_user_profile(user_profile)
        result = self.db_queries.get_user_profile('johndoe@gmail.com')
        self.assertEqual(result, user_profile)

    def test_create_travel_recommendation(self):
        travel_recommendation = TravelRecommendation('New York', 'London', 'Delta', 'Hilton', 'First Class', 'Wi-Fi')
        self.db_queries.create_travel_recommendation(travel_recommendation)
        result = self.db_queries.get_travel_recommendation('New York', 'London')
        self.assertEqual(result, travel_recommendation)

    def test_create_search_result(self):
        search_result = SearchResult('New York', 'London', 'Delta', 'Hilton', 'First Class', 'Wi-Fi')
        self.db_queries.create_search_result(search_result)
        result = self.db_queries.get_search_result('New York', 'London')
        self.assertEqual(result, search_result)

    def test_create_itinerary(self):
        itinerary = Itinerary('New York', 'London', 'Delta', 'Hilton', 'First Class', 'Wi-Fi')
        self.db_queries.create_itinerary(itinerary)
        result = self.db_queries.get_itinerary('New York', 'London')
        self.assertEqual(result, itinerary)

    def test_create_alert(self):
        alert = Alert('Flight Delay', 'Your flight has been delayed by 2 hours.')
        self.db_queries.create_alert(alert)
        result = self.db_queries.get_alert('Flight Delay')
        self.assertEqual(result, alert)

    def test_create_booking_detail(self):
        booking_detail = BookingDetail('John Doe', 'johndoe@gmail.com', 'Delta', 'Hilton', 'First Class', 'Wi-Fi')
        self.db_queries.create_booking_detail(booking_detail)
        result = self.db_queries.get_booking_detail('johndoe@gmail.com')
        self.assertEqual(result, booking_detail)

if __name__ == '__main__':
    unittest.main()
```