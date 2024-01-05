from flask import Flask
app = Flask(__name__)

@app.route("/")#root 
def home():
    return "Hello, Flask!"
