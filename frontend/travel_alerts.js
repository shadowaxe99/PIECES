```javascript
import { api } from './api.js';
import { alerts } from '../backend/travel_alerts.js';

// DOM Element
const alertBox = document.getElementById('alertBox');

// Function to display alerts
function displayAlerts() {
    alertBox.innerHTML = '';
    alerts.forEach(alert => {
        const alertElement = document.createElement('div');
        alertElement.classList.add('alert');
        alertElement.textContent = alert.message;
        alertBox.appendChild(alertElement);
    });
}

// Function to fetch alerts
async function fetchAlerts() {
    try {
        const response = await api.get('/alerts');
        if (response.status === 200) {
            alerts = response.data;
            displayAlerts();
        }
    } catch (error) {
        console.error('Error fetching alerts:', error);
    }
}

// Function to send alerts
async function sendAlert(alert) {
    try {
        const response = await api.post('/alerts', alert);
        if (response.status === 200) {
            alerts.push(alert);
            displayAlerts();
        }
    } catch (error) {
        console.error('Error sending alert:', error);
    }
}

// Listen for NEW_ALERT message
window.addEventListener('NEW_ALERT', (event) => {
    sendAlert(event.detail);
});

// Fetch alerts on page load
fetchAlerts();
```