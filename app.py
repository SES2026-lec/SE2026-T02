from flask import Flask

app = Flask(__name__)# 二人目

@app.route("/")
def hello():
    return "Hello World! I'm using Flask."
