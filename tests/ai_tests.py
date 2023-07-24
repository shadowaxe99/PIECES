```python
import unittest
from ai.recommendation_engine import generateRecommendations
from ai.data_processing import processUserData

class TestAI(unittest.TestCase):

    def setUp(self):
        self.userProfile = {
            "name": "John Doe",
            "preferences": {
                "airlines": "Delta",
                "hotel": "Marriott",
                "seat": "Economy",
                "amenities": ["Wi-Fi", "Window Seat"]
            },
            "pastTravelHistory": [
                {
                    "destination": "New York",
                    "airline": "Delta",
                    "hotel": "Marriott",
                    "activities": ["Statue of Liberty", "Central Park"]
                }
            ]
        }

    def test_generateRecommendations(self):
        recommendations = generateRecommendations(self.userProfile)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_processUserData(self):
        processedData = processUserData(self.userProfile)
        self.assertIsInstance(processedData, dict)
        self.assertIn('processedPreferences', processedData)
        self.assertIn('processedTravelHistory', processedData)

if __name__ == '__main__':
    unittest.main()
```