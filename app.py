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

    # Code 1: AI specialized in cloud infrastructure
    messages_code_1 = [
        {"role": "system", "content": "You are an AI specialized in cloud infrastructure."},
        {"role": "user", "content": user_message},
    ]

    model_response_code_1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_code_1
    )
    
    bot_response_code_1 = model_response_code_1['choices'][0]['message']['content']
    
    # Code 2: General purpose AI
    model_response_code_2 = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=user_message,
        max_tokens=150
    )

    # write chat history to a file (for Code 2)
    with open('/app/history/chat-history.txt', 'a') as file:
        file.write("User: " + user_message + "\n")
        file.write("AI: " + model_response_code_2.choices[0].text.strip() + "\n")

    if is_cloud_infrastructure_question(user_message):
        return jsonify({
            'message': bot_response_code_1,
        })
    else:
        return jsonify({
            'message': model_response_code_2.choices[0].text.strip(),
        })

def is_cloud_infrastructure_question(question):
    # Define conditions to identify cloud infrastructure questions
def is_cloud_infrastructure_question(question):
    # Define conditions to identify cloud infrastructure questions
    keywords = [
        'cloud', 'infrastructure', 'deploy', 'scale', 'network', 'devops', 'automation', 'script',
        'aws', 'azure', 'google cloud', 'ibm cloud', 'terraform', 'ansible', 'chef', 'puppet',
        'kubernetes', 'docker', 'serverless', 'load balancing', 'monitoring', 'security', 'backup',
        'database', 'virtualization', 'containers', 'microservices', 'architecture',
        'continuous integration', 'continuous deployment', 'version control', 'git', 'jenkins',
        'ci/cd', 'agile', 'devsecops', 'configuration management', 'orchestration', 'pipeline',
        'release management', 'testing automation', 'deployment pipeline', 'scrum', 'monitoring tools',
        'containerization', 'cloud-native', 'immutable infrastructure', 'blue-green deployment',
        'canary deployment', 'configuration as code', 'infrastructure as code', 'gitops', 'chatops',
        'site reliability engineering', 'incident management', 'log management', 'performance optimization',
        'elasticity', 'fault tolerance', 'high availability', 'cost optimization', 'compliance',
        'change management', 'release automation', 'service discovery', 'deployment strategy',
        'cloud migration', 'cloud security', 'cloud governance'
    ]

    for keyword in keywords:
        if keyword in question.lower():
            return True

    return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
