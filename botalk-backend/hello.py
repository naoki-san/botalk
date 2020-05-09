import json
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": os.environ.get("FRONTEND_ORIGIN", "http://localhost:*")}})


@app.route('/')
def hello():
    hello = "Hello world"
    return hello


@app.route('/message', methods=['POST'])
def message():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    response = chatbot.get_response(data["message"])
    data["message"] = str(response)
    return jsonify(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
