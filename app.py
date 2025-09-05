from flask import Flask, render_template
import os
import requests

app = Flask(__name__, template_folder="templates")

PORT = int(os.environ.get("PORT", 9000))
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")


@app.route("/")
def index():
    # get data from backend
    try:
        response = requests.get(f"{BACKEND_URL}/api/get")
        data = response.json()
    except Exception as e:
        data = {"data": [f"Error connecting to backend: {e}"]}

    env = dict(os.environ)
    return render_template("index.html", env=env, data=data.get("data", []))


if __name__ == "__main__":
    app.run(debug=True, port=PORT, host="0.0.0.0")
