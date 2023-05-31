document.getElementById('submitBtn').addEventListener('click', function() {
    var userInput = document.getElementById('userInput').value;
  
    // Display user's message
    var userMsgContainer = document.createElement('div');
    userMsgContainer.className = 'user-message';
    userMsgContainer.textContent = userInput;
    document.querySelector('.chatbox').appendChild(userMsgContainer);
  
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
    // ...

    .then(data => {
        // Display bot's message
        var botMsgContainer;
        if (isCode(data.message)) {
            botMsgContainer = document.createElement('pre');
            botMsgContainer.className = 'bot-message code language-python'; // set language as per your requirement
        
            // Add copy button
            var copyButton = document.createElement('button');
            copyButton.textContent = 'Copy Code';
            copyButton.className = 'copy-button';
            copyButton.addEventListener('click', function() {
                navigator.clipboard.writeText(data.message);
            });
            botMsgContainer.appendChild(copyButton);
        } else {
            botMsgContainer = document.createElement('div');
            botMsgContainer.className = 'bot-message';
        }
        var botMsgText = document.createElement('code');
        botMsgText.textContent = data.message;
        botMsgText.className = 'language-python'; // set language as per your requirement
        Prism.highlightElement(botMsgText);
        botMsgContainer.appendChild(botMsgText);
        document.querySelector('.chatbox').appendChild(botMsgContainer);
    });

    // Clear input field
    document.getElementById('userInput').value = '';
});

function isCode(str) {
    var codeKeywords = ['def', 'class', 'if', 'while', 'for', 'let', 'const', 'function', 'import', '#', '/*', '*/'];
    return codeKeywords.some(keyword => str.startsWith(keyword));
}
