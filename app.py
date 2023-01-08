import io
import pickle

from flask import Flask, request, send_file
import requests

app = Flask(__name__)


@app.route("/get", methods=["POST"])
def send_get():
    data = request.json
    r = requests.get(url=data.get("url", None))
    pickled_response = pickle.dumps(r)
    return send_file(io.BytesIO(pickled_response), mimetype="application/octet-stream")


@app.route("/post", methods=["POST"])
def send_post():
    data = request.json
    r = requests.post(url=data.get("url", None),
                      params=data.get("params", None),
                      json=data.get("json", None),
                      headers=data.get("headers", None),
                      timeout=data.get("timeout", None),
                      )

    pickled_response = pickle.dumps(r)
    return send_file(io.BytesIO(pickled_response), mimetype="application/octet-stream")


if __name__ == "__main__":
    app.run(debug=True)
