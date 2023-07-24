```python
from flask import Flask, request, jsonify
from user_profile import UserProfileSchema
from travel_recommendations import TravelRecommendationSchema
from real_time_search import SearchResultSchema
from itinerary_planner import ItinerarySchema
from travel_alerts import AlertSchema
from booking_integration import BookingDetailSchema

app = Flask(__name__)

@app.route('/user-profile', methods=['POST'])
def create_user_profile():
    data = request.get_json()
    user_profile = UserProfileSchema().load(data)
    return jsonify(user_profile), 201

@app.route('/travel-recommendations', methods=['GET'])
def get_travel_recommendations():
    user_profile = UserProfileSchema().load(request.args)
    travel_recommendations = TravelRecommendationSchema().dump(user_profile)
    return jsonify(travel_recommendations), 200

@app.route('/search', methods=['GET'])
def perform_real_time_search():
    search_criteria = request.args
    search_results = SearchResultSchema().dump(search_criteria)
    return jsonify(search_results), 200

@app.route('/itinerary', methods=['POST', 'PUT'])
def plan_itinerary():
    data = request.get_json()
    itinerary = ItinerarySchema().load(data)
    return jsonify(itinerary), 201

@app.route('/alerts', methods=['GET'])
def get_alerts():
    user_profile = UserProfileSchema().load(request.args)
    alerts = AlertSchema().dump(user_profile)
    return jsonify(alerts), 200

@app.route('/booking', methods=['POST'])
def process_booking():
    data = request.get_json()
    booking_details = BookingDetailSchema().load(data)
    return jsonify(booking_details), 201

if __name__ == '__main__':
    app.run(debug=True)
```