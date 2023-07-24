```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/travel_booker'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    preferences = db.Column(db.JSON, nullable=False)
    loyalty_programs = db.Column(db.JSON)
    past_travel_history = db.Column(db.JSON)

    def __init__(self, name, email, preferences, loyalty_programs, past_travel_history):
        self.name = name
        self.email = email
        self.preferences = preferences
        self.loyalty_programs = loyalty_programs
        self.past_travel_history = past_travel_history

class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'preferences', 'loyalty_programs', 'past_travel_history')

user_profile_schema = UserProfileSchema()
user_profiles_schema = UserProfileSchema(many=True)

@app.route('/user_profile', methods=['POST'])
def add_user_profile():
    name = request.json['name']
    email = request.json['email']
    preferences = request.json['preferences']
    loyalty_programs = request.json['loyalty_programs']
    past_travel_history = request.json['past_travel_history']

    new_user_profile = UserProfile(name, email, preferences, loyalty_programs, past_travel_history)

    db.session.add(new_user_profile)
    db.session.commit()

    return user_profile_schema.jsonify(new_user_profile)

@app.route('/user_profile/<id>', methods=['GET'])
def get_user_profile(id):
    user_profile = UserProfile.query.get(id)
    return user_profile_schema.jsonify(user_profile)

@app.route('/user_profile/<id>', methods=['PUT'])
def update_user_profile(id):
    user_profile = UserProfile.query.get(id)

    name = request.json['name']
    email = request.json['email']
    preferences = request.json['preferences']
    loyalty_programs = request.json['loyalty_programs']
    past_travel_history = request.json['past_travel_history']

    user_profile.name = name
    user_profile.email = email
    user_profile.preferences = preferences
    user_profile.loyalty_programs = loyalty_programs
    user_profile.past_travel_history = past_travel_history

    db.session.commit()

    return user_profile_schema.jsonify(user_profile)

if __name__ == '__main__':
    app.run(debug=True)
```