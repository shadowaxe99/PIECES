```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    preferences = Column(String)
    loyalty_programs = Column(String)
    past_travel_history = Column(String)

class TravelRecommendation(Base):
    __tablename__ = 'travel_recommendations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    recommendations = Column(String)

class BookingDetail(Base):
    __tablename__ = 'booking_details'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    booking_info = Column(String)

engine = create_engine('postgresql://user:password@localhost:5432/travel_booker')
Session = sessionmaker(bind=engine)

def get_db_session():
    session = Session()
    return session

def init_db():
    Base.metadata.create_all(engine)
```
