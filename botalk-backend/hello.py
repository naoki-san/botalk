import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

app = Flask(__name__)
CORS(app)


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
    app.run()
