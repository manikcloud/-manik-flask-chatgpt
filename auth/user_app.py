from flask import Flask, request, render_template, redirect, session
from flask_bcrypt import Bcrypt
from boto3.dynamodb.conditions import Key  # Add this line
import boto3
from botocore.exceptions import ClientError
import uuid
import datetime
import os  # Add this line

app = Flask(__name__, static_folder='static', static_url_path='/static')
bcrypt = Bcrypt(app)

app.secret_key = os.urandom(24)  # Add this line

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table("manik-gpt-auth")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        sex = request.form['sex']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        id = str(uuid.uuid4())  # generate a UUID string as id

        try:
            table.put_item(
                Item={
                    'id': id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'sex': sex,
                    'email': email,
                    'password': password
                }
            )
            return "Signed up successfully, go to the login page."
        except ClientError as e:
            print("Error inserting into DynamoDB:", str(e))
            return "Error occurred while signing up", 500
    else:  # GET request
        return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    try:
        response = table.query(
            IndexName='EmailIndex',
            KeyConditionExpression=Key('email').eq(email)
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return "Error occurred while logging in", 500
    else:
        items = response.get('Items')
        if items:
            user = items[0]  # Get the first user that matches the email
            stored_password = user.get('password')
            if bcrypt.check_password_hash(stored_password, password):
                first_name = user.get('first_name')
                current_date = datetime.datetime.now().strftime('%d-%m-%Y')
                return render_template('login.html', first_name=first_name, current_date=current_date)
        return "Invalid email or password"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
