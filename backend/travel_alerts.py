```python
from flask import Flask, jsonify, request
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')

client = Client(account_sid, auth_token)

alerts = []

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)

@app.route('/alerts', methods=['POST'])
def create_alert():
    alert_data = request.get_json()
    alerts.append(alert_data)
    send_alert(alert_data)
    return jsonify(alert_data), 201

def send_alert(alert_data):
    message = client.messages.create(
        body=alert_data['message'],
        from_=twilio_number,
        to=alert_data['phone_number']
    )
    print(f"Sent alert: {message.sid}")

if __name__ == '__main__':
    app.run(debug=True)
```