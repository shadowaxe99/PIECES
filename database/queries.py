```python
from models import UserProfile, TravelRecommendation, SearchResult, Itinerary, Alert, BookingDetail
from sqlalchemy.orm import Session

def get_user_profile(session: Session, user_id: int):
    return session.query(UserProfile).filter(UserProfile.id == user_id).first()

def get_travel_recommendations(session: Session, user_id: int):
    return session.query(TravelRecommendation).filter(TravelRecommendation.user_id == user_id).all()

def get_search_results(session: Session, search_id: int):
    return session.query(SearchResult).filter(SearchResult.id == search_id).first()

def get_itinerary(session: Session, itinerary_id: int):
    return session.query(Itinerary).filter(Itinerary.id == itinerary_id).first()

def get_alerts(session: Session, user_id: int):
    return session.query(Alert).filter(Alert.user_id == user_id).all()

def get_booking_details(session: Session, booking_id: int):
    return session.query(BookingDetail).filter(BookingDetail.id == booking_id).first()

def create_user_profile(session: Session, user_profile: UserProfile):
    session.add(user_profile)
    session.commit()
    return user_profile

def create_travel_recommendation(session: Session, travel_recommendation: TravelRecommendation):
    session.add(travel_recommendation)
    session.commit()
    return travel_recommendation

def create_search_result(session: Session, search_result: SearchResult):
    session.add(search_result)
    session.commit()
    return search_result

def create_itinerary(session: Session, itinerary: Itinerary):
    session.add(itinerary)
    session.commit()
    return itinerary

def create_alert(session: Session, alert: Alert):
    session.add(alert)
    session.commit()
    return alert

def create_booking_detail(session: Session, booking_detail: BookingDetail):
    session.add(booking_detail)
    session.commit()
    return booking_detail
```