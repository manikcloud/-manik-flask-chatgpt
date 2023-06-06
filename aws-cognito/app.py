from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap
import boto3
import os

app = Flask(__name__)
secret_key = os.urandom(16).hex()
print(secret_key)
bootstrap = Bootstrap(app)

# AWS Cognito configuration
AWS_REGION = 'us-east-1'
COGNITO_POOL_ID = 'us-east-1_cap03qDQv'
COGNITO_CLIENT_ID = '1isns7i7v5m6f91e0n8qapgahr'
COGNITO_DOMAIN = 'https://manikgpt.auth.us-east-1.amazoncognito.com'

# Create AWS Cognito client
client = boto3.client('cognito-idp', region_name=AWS_REGION)

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

        # Create user in Cognito User Pool
        try:
            response = client.sign_up(
                ClientId=COGNITO_CLIENT_ID,
                Username=email,
                Password=password,
                UserAttributes=[
                    {'Name': 'given_name', 'Value': first_name},
                    {'Name': 'family_name', 'Value': last_name},
                    {'Name': 'email', 'Value': email}
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
