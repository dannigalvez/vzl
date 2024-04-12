from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Homepage"

@app.route('/contact')
def contact():
    return "Contact page"
