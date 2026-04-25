from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("received:", data)
    return "OK", 200
