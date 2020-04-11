import json

from flask import Flask, request, jsonify
from flask_cors import CORS

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
    return jsonify(data)


if __name__ == "__main__":
    app.run()
