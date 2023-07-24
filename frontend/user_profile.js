```javascript
// Importing necessary libraries
import axios from 'axios';

// DOM Elements
const userProfileForm = document.getElementById('userProfileForm');

// Event Listener for form submission
userProfileForm.addEventListener('submit', createUserProfile);

// Function to create user profile
function createUserProfile(event) {
    event.preventDefault();

    // Get form data
    const formData = new FormData(userProfileForm);
    const userProfile = Object.fromEntries(formData);

    // Send POST request to backend
    axios.post('/api/user_profile', userProfile)
        .then(response => {
            if(response.status === 200) {
                // Update userProfile variable
                window.userProfile = response.data;

                // Dispatch event
                const event = new CustomEvent('USER_PROFILE_UPDATED', { detail: window.userProfile });
                window.dispatchEvent(event);
            }
        })
        .catch(error => {
            console.error('Error creating user profile:', error);
        });
}
```