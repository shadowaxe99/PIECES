```javascript
import { api } from './api.js';

let travelRecommendations = [];

// Function to generate travel recommendations
export function generateRecommendations(userProfile) {
    api.getRecommendations(userProfile)
        .then(response => {
            travelRecommendations = response.data;
            displayRecommendations();
        })
        .catch(error => {
            console.error('Error generating recommendations:', error);
        });
}

// Function to display travel recommendations
function displayRecommendations() {
    const recommendationList = document.getElementById('recommendationList');
    recommendationList.innerHTML = '';

    travelRecommendations.forEach(recommendation => {
        const listItem = document.createElement('li');
        listItem.textContent = `${recommendation.destination}: ${recommendation.description}`;
        recommendationList.appendChild(listItem);
    });
}

// Listen for the USER_PROFILE_UPDATED event
document.addEventListener('USER_PROFILE_UPDATED', (event) => {
    generateRecommendations(event.detail);
});
```