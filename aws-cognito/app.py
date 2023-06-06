from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap
import boto3
import os
import hmac
import hashlib
import base64

app = Flask(__name__)
secret_key = os.urandom(16).hex()
print(secret_key)
bootstrap = Bootstrap(app)

# AWS Cognito configuration
AWS_REGION = 'us-east-1'
COGNITO_POOL_ID = os.getenv('COGNITO_POOL_ID')
COGNITO_CLIENT_ID = os.getenv('COGNITO_CLIENT_ID')
COGNITO_CLIENT_SECRET = os.getenv('COGNITO_CLIENT_SECRET') # Replace with your Cognito Client Secret
COGNITO_DOMAIN = 'https://manikgpt.auth.us-east-1.amazoncognito.com'

# Create AWS Cognito client
client = boto3.client('cognito-idp', region_name=AWS_REGION)

def get_secret_hash(username):
    msg = username + COGNITO_CLIENT_ID
    dig = hmac.new(str.encode(COGNITO_CLIENT_SECRET), msg=str.encode(msg), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        birthdate = request.form['birthdate']

        # Create user in Cognito User Pool
        try:
            response = client.sign_up(
                ClientId=COGNITO_CLIENT_ID,
                SecretHash=calculate_secret_hash(COGNITO_CLIENT_ID, COGNITO_CLIENT_SECRET, email),
                Username=email,
                Password=password,
                UserAttributes=[
                    {'Name': 'given_name', 'Value': first_name},
                    {'Name': 'family_name', 'Value': last_name},
                    {'Name': 'email', 'Value': email},
                    {'Name': 'gender', 'Value': gender},
                    {'Name': 'birthdate', 'Value': birthdate}
                ]
            )
            return redirect(url_for('login'))
        except client.exceptions.UsernameExistsException:
            error_message = 'Email already exists. Please try a different email.'
            return render_template('signup.html', error_message=error_message)
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            response = client.initiate_auth(
                ClientId=COGNITO_CLIENT_ID,
                SecretHash=get_secret_hash(email),
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': email,
                    'PASSWORD': password
                }
            )
            session['access_token'] = response['AuthenticationResult']['AccessToken']
            return redirect(url_for('dashboard'))
        except client.exceptions.NotAuthorizedException:
            error_message = 'Invalid email or password. Please try again.'
            return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'access_token' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
