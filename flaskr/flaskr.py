from flask import Flask, request, render_template, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/<url>')
def get_url(url=None):
    return render_template(url)
