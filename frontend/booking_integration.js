```javascript
import axios from 'axios';
import { bookingDetails } from './api.js';

const bookingForm = document.getElementById('bookingForm');

bookingForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(bookingForm);
  const bookingData = Object.fromEntries(formData);

  try {
    const response = await axios.post(bookingDetails, bookingData);
    if (response.status === 200) {
      alert('Booking confirmed!');
      document.dispatchEvent(new CustomEvent('BOOKING_CONFIRMED', { detail: bookingData }));
    } else {
      alert('Booking failed. Please try again.');
    }
  } catch (error) {
    console.error('Error during booking:', error);
    alert('Booking failed. Please try again.');
  }
});
```