```python
from sklearn.ensemble import RandomForestRegressor
from database.models import UserProfile, TravelRecommendation
from database.queries import get_user_profile, get_past_travel_data

def generate_recommendations(user_id):
    # Fetch user profile and past travel data
    user_profile = get_user_profile(user_id)
    past_travel_data = get_past_travel_data(user_id)

    # Prepare data for recommendation engine
    X = past_travel_data.drop('destination', axis=1)
    y = past_travel_data['destination']

    # Train the recommendation engine
    recommendation_engine = RandomForestRegressor(n_estimators=100, random_state=42)
    recommendation_engine.fit(X, y)

    # Generate recommendations based on user profile
    recommendations = recommendation_engine.predict(user_profile)

    # Create TravelRecommendation objects and save to database
    travel_recommendations = [TravelRecommendation(user_id=user_id, destination=rec) for rec in recommendations]
    for rec in travel_recommendations:
        rec.save()

    return travel_recommendations
```