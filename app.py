from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://chatgpt:chatgpt@db/chatgpt'
# db = SQLAlchemy(app)

# class Chat(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_message = db.Column(db.String(500))
#     bot_response = db.Column(db.String(500))

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

    # Store the user message and bot response in the database
    # new_chat = Chat(user_message=user_message, bot_response=bot_response)
    # db.session.add(new_chat)
    # db.session.commit()

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
        "cloud",
        "infrastructure",
        "deploy",
        "scale",
        "network",
        "devops",
        "automation",
        "script",
        "aws",
        "azure",
        "google cloud",
        "ibm cloud",
        "terraform",
        "ansible",
        "chef",
        "puppet",
        "kubernetes",
        "docker",
        "serverless",
        "load balancing",
        "monitoring",
        "security",
        "backup",
        "database",
        "virtualization",
        "containers",
        "microservices",
        "architecture",
        "continuous integration",
        "continuous deployment",
        "version control",
        "git",
        "jenkins",
        "ci/cd",
        "agile",
        "devsecops",
        "configuration management",
        "orchestration",
        "pipeline",
        "release management",
        "testing automation",
        "deployment pipeline",
        "scrum",
        "monitoring tools",
        "containerization",
        "cloud-native",
        "immutable infrastructure",
        "blue-green deployment",
        "canary deployment",
        "configuration as code",
        "infrastructure as code",
        "gitops",
        "chatops",
        "site reliability engineering",
        "incident management",
        "log management",
        "performance optimization",
        "elasticity",
        "fault tolerance",
        "high availability",
        "cost optimization",
        "compliance",
        "change management",
        "release automation",
        "service discovery",
        "deployment strategy",
        "cloud migration",
        "cloud security",
        "cloud governance",
    ]

    for keyword in keywords:
        if keyword in question.lower():
            return True

    return False

# db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
