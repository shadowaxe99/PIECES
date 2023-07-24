```javascript
import jwt from 'jsonwebtoken';

const SECRET_KEY = 'your-secret-key'; // Replace with your actual secret key

export function authenticateUser(username, password) {
  // This is a placeholder function. In a real application, you would verify the username and password against your user database.
  if (username && password) {
    const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
    return token;
  } else {
    throw new Error('Invalid username or password');
  }
}

export function verifyToken(token) {
  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    return decoded.username;
  } catch (err) {
    throw new Error('Invalid token');
  }
}

export function checkAuthentication() {
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error('Not authenticated');
  }

  const username = verifyToken(token);
  return username;
}
```