```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    travel_preferences = Column(String)
    loyalty_programs = Column(String)
    past_travel_history = Column(String)

class TravelRecommendation(Base):
    __tablename__ = 'travel_recommendations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    flights = Column(String)
    accommodations = Column(String)
    activities = Column(String)
    dining_options = Column(String)

class SearchResult(Base):
    __tablename__ = 'search_results'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    flights = Column(String)
    hotels = Column(String)
    rental_cars = Column(String)

class Itinerary(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    travel_plan = Column(String)

class Alert(Base):
    __tablename__ = 'alerts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    message = Column(String)

class BookingDetail(Base):
    __tablename__ = 'booking_details'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    booking_info = Column(String)
    payment_info = Column(String)
```
