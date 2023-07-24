```python
from flask import Flask, request, jsonify
from database import db_session
from database.models import BookingDetailSchema, Booking
from security import authenticate_user

app = Flask(__name__)

@app.route('/booking', methods=['POST'])
@authenticate_user
def process_booking():
    booking_details = request.get_json()
    errors = BookingDetailSchema().validate(booking_details)
    if errors:
        return jsonify(errors), 400

    booking = Booking(**booking_details)
    db_session.add(booking)
    db_session.commit()

    return jsonify(BookingDetailSchema().dump(booking)), 201

@app.route('/booking/<int:booking_id>', methods=['GET'])
@authenticate_user
def get_booking(booking_id):
    booking = db_session.query(Booking).get(booking_id)
    if booking is None:
        return jsonify({'message': 'Booking not found'}), 404

    return jsonify(BookingDetailSchema().dump(booking)), 200

@app.route('/booking/<int:booking_id>', methods=['DELETE'])
@authenticate_user
def delete_booking(booking_id):
    booking = db_session.query(Booking).get(booking_id)
    if booking is None:
        return jsonify({'message': 'Booking not found'}), 404

    db_session.delete(booking)
    db_session.commit()

    return jsonify({'message': 'Booking deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```