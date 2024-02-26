// script.js
const backendURL = 'http://localhost:3000';

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    
    // Simulate backend request
    fetch(backendURL +'/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/success.html';
        } else {
            document.getElementById('errorMessage').textContent = 'Email or password is wrong.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function handleCredentialResponse(response) {
    const credential = response.credential;
    // Check if the response contains the Google ID token
    if (credential) {
        // Redirect to success.html
        window.location.href = '/success.html';
    } else {
        // Handle error or do nothing
        console.error('Google Sign-In failed');
    }
}

// Other code for handling login form submission, etc.

