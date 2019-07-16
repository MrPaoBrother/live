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
    return render_template('video.html')


@app.route('/live')
def live():
    with open("./static/video_data/test.m3u8", "rb") as fs:
        lines = "".join(fs.readlines())
    response = make_response(lines)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    print response.response
    return response


@app.route('/get_ts/<filename>')
def get_ts(filename):
    d = "./static/video_data/"
    response = make_response(send_from_directory(d, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
