document.getElementById('submitBtn').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keydown', function(e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        sendMessage();
    }
});

function isCode(str) {
    var codeKeywords = ['def', 'class', 'if', 'while', 'for', 'let', 'const', 'function', 'import', '#', '/*', '*/'];
    return codeKeywords.some(keyword => str.startsWith(keyword));
}

function sendMessage() {
    var userInput = document.getElementById('userInput').value;
    displayUserMessage(userInput);
    getResponse(userInput);
    document.getElementById('userInput').value = '';
}

function displayUserMessage(message) {
    var userMsgContainer = document.createElement('div');
    userMsgContainer.className = 'user-message';
    userMsgContainer.textContent = message;
    document.querySelector('.chatbox').appendChild(userMsgContainer);
    addToLocalStorage('user', message);
}

function displayBotMessage(message, isCodeBlock) {
    var botMsgContainer;
    if (isCodeBlock) {
        botMsgContainer = document.createElement('pre');
        botMsgContainer.className = 'bot-message code language-python'; // set language as per your requirement

        // Add copy button
        var copyButton = document.createElement('button');
        copyButton.textContent = 'Copy Code';
        copyButton.className = 'copy-button';
        copyButton.onclick = function() {
            navigator.clipboard.writeText(message);
        };
        botMsgContainer.appendChild(copyButton);
    } else {
        botMsgContainer = document.createElement('div');
        botMsgContainer.className = 'bot-message';
    }
    var botMsgText = document.createElement('code');
    botMsgText.textContent = message;
    botMsgText.className = 'language-python'; // set language as per your requirement
    Prism.highlightElement(botMsgText);
    botMsgContainer.appendChild(botMsgText);
    document.querySelector('.chatbox').appendChild(botMsgContainer);
    addToLocalStorage('bot', message);
}

function getResponse(message) {
    fetch('/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'message': message
      }),
    })
    .then(response => response.json())
    .then(data => {
        var isCodeBlock = isCode(data.message);
        displayBotMessage(data.message, isCodeBlock);
    });
}

function addToLocalStorage(sender, message) {
    var chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.push({sender: sender, message: message});
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
}

window.onload = function() {
    var chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.forEach(chat => {
        if (chat.sender === 'user') {
            displayUserMessage(chat.message);
        } else if (chat.sender === 'bot') {
            var isCodeBlock = isCode(chat.message);
            displayBotMessage(chat.message, isCodeBlock);
        }
    });
}
