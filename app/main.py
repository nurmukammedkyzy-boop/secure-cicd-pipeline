from flask import Flask, request, jsonify
import logging
import os
import re
from datetime import datetime

app = Flask(__name__)

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_ENV = os.getenv("APP_ENV", "development")
SECRET_TOKEN = os.getenv("APP_SECRET_TOKEN", "not-set")


def is_valid_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,20}", username))


@app.route("/", methods=["GET"])
def home():
    logging.info("Home endpoint accessed")
    return jsonify({
        "message": "Secure CI/CD Demo API",
        "environment": API_ENV,
        "status": "running"
    })


@app.route("/greet", methods=["POST"])
def greet_user():
    data = request.get_json()

    if not data or "username" not in data:
        logging.warning("Invalid request: username missing")
        return jsonify({"error": "username is required"}), 400

    username = data["username"]

    if not is_valid_username(username):
        logging.warning("Invalid username input detected")
        return jsonify({
            "error": "Invalid username. Use 3-20 letters, numbers, or underscores only."
        }), 400

    logging.info("User greeted successfully")
    return jsonify({"message": f"Hello, {username}!"})


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    if not data or "a" not in data or "b" not in data or "operation" not in data:
        logging.warning("Invalid calculation request")
        return jsonify({"error": "a, b, and operation are required"}), 400

    try:
        a = float(data["a"])
        b = float(data["b"])
    except ValueError:
        logging.warning("Non-numeric input detected")
        return jsonify({"error": "a and b must be numbers"}), 400

    operation = data["operation"]

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            logging.warning("Division by zero attempt")
            return jsonify({"error": "division by zero is not allowed"}), 400
        result = a / b
    else:
        logging.warning("Unsupported operation requested")
        return jsonify({"error": "unsupported operation"}), 400

    logging.info("Calculation completed successfully")
    return jsonify({"result": result})


@app.route("/health", methods=["GET"])
def health_check():
    logging.info("Health check executed")
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": API_ENV
    })


@app.route("/secure-info", methods=["GET"])
def secure_info():
    if SECRET_TOKEN == "not-set":
        logging.warning("Secret token is not configured")
        return jsonify({"error": "secret token is not configured"}), 500

    logging.info("Secure info endpoint accessed")
    return jsonify({
        "message": "Secret is loaded securely from environment variable",
        "token_loaded": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)