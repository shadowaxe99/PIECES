```python
from flask import Flask, request, jsonify
from database.models import ItinerarySchema, UserProfileSchema
from database.queries import get_user_profile
from ai.recommendation_engine import optimize_itinerary

app = Flask(__name__)

@app.route('/itinerary', methods=['POST'])
def plan_itinerary():
    user_id = request.json.get('user_id')
    user_profile = get_user_profile(user_id)
    if not user_profile:
        return jsonify({"error": "User profile not found"}), 404

    UserProfileSchema().load(user_profile)
    itinerary = request.json.get('itinerary')
    ItinerarySchema().load(itinerary)

    optimized_itinerary = optimize_itinerary(user_profile, itinerary)
    return jsonify(optimized_itinerary), 200

@app.route('/itinerary', methods=['PUT'])
def update_itinerary():
    user_id = request.json.get('user_id')
    user_profile = get_user_profile(user_id)
    if not user_profile:
        return jsonify({"error": "User profile not found"}), 404

    UserProfileSchema().load(user_profile)
    itinerary = request.json.get('itinerary')
    ItinerarySchema().load(itinerary)

    updated_itinerary = optimize_itinerary(user_profile, itinerary)
    return jsonify(updated_itinerary), 200
```