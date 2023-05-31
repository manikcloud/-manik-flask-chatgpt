document.getElementById('submitBtn').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keyup', function(event) {
    if (event.keyCode === 13) {
        sendMessage();
    }
});

function sendMessage() {
    var userInput = document.getElementById('userInput').value;

    // Display user's message
    var userMsgContainer = document.createElement('div');
    userMsgContainer.className = 'user-message';
    userMsgContainer.textContent = userInput;
    document.querySelector('.chatbox').appendChild(userMsgContainer);

    // Save chat history
    localStorage.setItem('chatHistory', document.querySelector('.chatbox').innerHTML);

    // Send message to backend and get response
    fetch('/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'message': userInput
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display bot's message
        var botMsgContainer;
        if (data.message) {
            botMsgContainer = document.createElement('pre');
            botMsgContainer.className = 'bot-message code language-python';

            // Add copy button
            var copyButton = document.createElement('button');
            copyButton.textContent = 'Copy Code';
            copyButton.className = 'copy-button';
            copyButton.onclick = function() {
                copyToClipboard(data.message);
            };
            botMsgContainer.appendChild(copyButton);

            var botMsgText = document.createElement('code');
            botMsgText.textContent = data.message;
            botMsgText.className = 'language-python';
            Prism.highlightElement(botMsgText);
            botMsgContainer.appendChild(botMsgText);
        } else {
            botMsgContainer = document.createElement('div');
            botMsgContainer.className = 'bot-message';
        }

        document.querySelector('.chatbox').appendChild(botMsgContainer);

        // Save chat history
        localStorage.setItem('chatHistory', document.querySelector('.chatbox').innerHTML);
    });

    // Clear input field
    document.getElementById('userInput').value = '';
}

function copyToClipboard(text) {
    var tempTextArea = document.createElement('textarea');
    tempTextArea.value = text;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
    console.log('Code copied to clipboard!');
}

// Load chat history
window.onload = function() {
    var chatHistory = localStorage.getItem('chatHistory');
    if (chatHistory) {
        document.querySelector('.chatbox').innerHTML = chatHistory;
    }
};
