import flask

app = flask.Flask(__name__)


@app.route('/article', methods=['GET'])
def article():
    response = flask.jsonify(title="Article title", content="Some important content")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


app.run()