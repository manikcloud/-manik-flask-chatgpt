from flask import Flask, request, jsonify, render_template
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def chat_message():
    user_message = request.json['message']
    messages = [
        {
            "role": "system",
            "content": "You are an AI specialized in cloud infrastructure.",
        },
        {"role": "user", "content": user_message},
    ]

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
    )

    bot_response = response['choices'][0]['message']['content']

    if is_cloud_infrastructure_question(user_message):
        return jsonify({
            'message': bot_response,
        })
    else:
        return jsonify({
            'message': 'Please ask a cloud infrastructure-related question.',
        })

def is_cloud_infrastructure_question(question):
    # Define conditions to identify cloud infrastructure questions
    keywords = [
        "cloud",
        "infrastructure",
        "deploy",
        "scale",
        "network",
    ]

    for keyword in keywords:
        if keyword in question.lower():
            return True

    return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
