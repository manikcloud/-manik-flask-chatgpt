from flask import Flask, request, render_template
import bcrypt
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table("manik-gpt-auth")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password'].encode('utf-8')

    try:
        response = table.get_item(
            Key={
                'email': email
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        hashed_password = item['password'].encode('utf-8')
        if bcrypt.checkpw(password, hashed_password):
            return "Logged in successfully"
        else:
            return "Password is incorrect"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
