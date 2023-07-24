```javascript
// Importing axios for making HTTP requests
import axios from 'axios';

// Base URL for the backend API
const API_BASE_URL = 'http://localhost:5000/api';

// Function to create a new user profile
export const createUserProfile = async (userProfile) => {
  const response = await axios.post(`${API_BASE_URL}/userProfile`, userProfile);
  return response.data;
};

// Function to generate personalized travel recommendations
export const generateRecommendations = async (userPreferences) => {
  const response = await axios.post(`${API_BASE_URL}/travelRecommendations`, userPreferences);
  return response.data;
};

// Function to perform real-time travel search
export const performRealTimeSearch = async (searchCriteria) => {
  const response = await axios.post(`${API_BASE_URL}/realTimeSearch`, searchCriteria);
  return response.data;
};

// Function to plan and optimize travel itinerary
export const planItinerary = async (itineraryDetails) => {
  const response = await axios.post(`${API_BASE_URL}/itineraryPlanner`, itineraryDetails);
  return response.data;
};

// Function to send personalized travel alerts
export const sendAlert = async (alertDetails) => {
  const response = await axios.post(`${API_BASE_URL}/travelAlerts`, alertDetails);
  return response.data;
};

// Function to process booking and payment
export const processBooking = async (bookingDetails) => {
  const response = await axios.post(`${API_BASE_URL}/bookingIntegration`, bookingDetails);
  return response.data;
};
```