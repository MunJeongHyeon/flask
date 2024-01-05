from flask import Flask
app = Flask(__name__)

@app.route("/")#root 
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, True)
