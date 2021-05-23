import flask
from flask import render_template, request, json

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("main-page.html")


@app.route('/xml', methods=['GET'])
def home_xml():
    return render_template("xml-page.html")


if __name__ == "__main__":
    app.run()
