// Function to process the user query
function processQuery() {
    const userInput = document.getElementById('userInput').value;
    if (!userInput) return;

    // Add user query to chat
    addMessage('user', userInput);

    // Send query to the server
    fetch('http://localhost:5000/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Show no results message if no products found
            addMessage('bot', data.message);
        } else {
            // Display product details
            data.forEach(product => {
                addMessage('bot', `Product: ${product.name} <br> Price: ${product.price} <br> Description: ${product.description}`);
            });
        }
    })
    .catch(error => {
        addMessage('bot', 'Sorry, something went wrong.');
        console.error('Error:', error);
    });
}

// Function to add message to chat
function addMessage(sender, message) {
    const chatContainer = document.getElementById('chatContainer');
    const messageElement = document.createElement('div');
    messageElement.classList.add(sender);
    messageElement.innerHTML = message;
    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;  // Scroll to bottom
}
