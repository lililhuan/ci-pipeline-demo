from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@app.route("/")
def home():
    return jsonify({"message": "Hello from my app!"})