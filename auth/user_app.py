from flask import Flask, request, render_template
from flask_bcrypt import Bcrypt
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
bcrypt = Bcrypt(app)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("manik-gpt-auth")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

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
        if bcrypt.check_password_hash(item['password'], password):
            return "Logged in successfully"
        else:
            return "Password is incorrect"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
