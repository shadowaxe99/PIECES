```javascript
import { userProfile, itinerary } from './user_profile.js';
import { api } from './api.js';

const itineraryPlanner = document.getElementById('itineraryPlanner');

function planItinerary() {
    const userPreferences = userProfile.preferences;
    const travelDates = userProfile.travelDates;

    api.getRecommendations(userPreferences, travelDates)
        .then(recommendations => {
            itinerary.activities = recommendations.activities;
            itinerary.flights = recommendations.flights;
            itinerary.hotels = recommendations.hotels;
            updateItineraryDisplay();
        })
        .catch(error => console.error('Error:', error));
}

function updateItineraryDisplay() {
    itineraryPlanner.innerHTML = '';

    itinerary.flights.forEach(flight => {
        const flightElement = document.createElement('div');
        flightElement.textContent = `Flight: ${flight.airline} ${flight.flightNumber} from ${flight.departure} to ${flight.destination}`;
        itineraryPlanner.appendChild(flightElement);
    });

    itinerary.hotels.forEach(hotel => {
        const hotelElement = document.createElement('div');
        hotelElement.textContent = `Hotel: ${hotel.name} in ${hotel.location}`;
        itineraryPlanner.appendChild(hotelElement);
    });

    itinerary.activities.forEach(activity => {
        const activityElement = document.createElement('div');
        activityElement.textContent = `Activity: ${activity.name} in ${activity.location}`;
        itineraryPlanner.appendChild(activityElement);
    });
}

export { planItinerary };
```