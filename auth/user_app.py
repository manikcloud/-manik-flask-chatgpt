from flask import Flask, request, render_template, redirect, url_for
from flask_bcrypt import Bcrypt
import boto3
from botocore.exceptions import ClientError
import uuid

app = Flask(__name__, static_folder='static', static_url_path='/static')
bcrypt = Bcrypt(app)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table("manik-gpt-auth")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        sex = request.form['sex']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'sex': sex,
            }
        )

        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

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
