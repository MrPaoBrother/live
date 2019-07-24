# -*- coding:utf8 -*-

from flask import Flask
from flask import render_template
from flask import make_response, jsonify
from flask import Flask, request, jsonify, send_from_directory, abort
from flask_cors import CORS
from flask_cors import cross_origin
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
@cross_origin()
def hello_world():
    return render_template('rtmp.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
