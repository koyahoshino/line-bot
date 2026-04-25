from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json
    print("===== webhook received =====")
    print(body)  # ← 受け取った内容をログに出す
    return "OK"

# Render用（ローカルでも起動できる）
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)