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
    .then(data => {
      // Display bot's message
      var botMsgContainer = document.createElement('div');
      botMsgContainer.className = 'bot-message';
      botMsgContainer.textContent = data.message;
      document.querySelector('.chatbox').appendChild(botMsgContainer);
    });
  });
  