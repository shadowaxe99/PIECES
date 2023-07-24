```python
import unittest
from backend.app import app
from backend.user_profile import UserProfile
from backend.travel_recommendations import TravelRecommendations
from backend.real_time_search import RealTimeSearch
from backend.itinerary_planner import ItineraryPlanner
from backend.travel_alerts import TravelAlerts
from backend.booking_integration import BookingIntegration

class BackendTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.userProfile = UserProfile()
        self.travelRecommendations = TravelRecommendations()
        self.realTimeSearch = RealTimeSearch()
        self.itineraryPlanner = ItineraryPlanner()
        self.travelAlerts = TravelAlerts()
        self.bookingIntegration = BookingIntegration()

    def test_user_profile_creation(self):
        response = self.userProfile.create_user_profile()
        self.assertEqual(response.status_code, 200)

    def test_travel_recommendations(self):
        response = self.travelRecommendations.generate_recommendations()
        self.assertEqual(response.status_code, 200)

    def test_real_time_search(self):
        response = self.realTimeSearch.perform_real_time_search()
        self.assertEqual(response.status_code, 200)

    def test_itinerary_planner(self):
        response = self.itineraryPlanner.plan_itinerary()
        self.assertEqual(response.status_code, 200)

    def test_travel_alerts(self):
        response = self.travelAlerts.send_alert()
        self.assertEqual(response.status_code, 200)

    def test_booking_integration(self):
        response = self.bookingIntegration.process_booking()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```