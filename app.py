from flask import Flask

app = Flask(__name__)# 二人目

@app.route("/") #三人目
def hello():
    return "Hello World! I'm using Flask."#三人目
    #一人目
    #二人目
