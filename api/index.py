from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the chamber.'

@app.route('/about')
def about():
    return 'About'
