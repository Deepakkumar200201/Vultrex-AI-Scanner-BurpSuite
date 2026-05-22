from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAPID_API_KEY = "Your api key"
RAPID_API_URL = "https://claude-3-7-sonnet.p.rapidapi.com/"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json

        headers = {
            "x-rapidapi-key": RAPID_API_KEY,
            "x-rapidapi-host": "claude-3-7-sonnet.p.rapidapi.com",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.post(RAPID_API_URL, json=data, headers=headers, timeout=60)

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
