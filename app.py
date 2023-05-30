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
    model_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        max_tokens=150
    )

    return jsonify({
        'message': model_response.choices[0].text.strip(),
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
