from flask import Flask, render_template
from gphotospy import authorize

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')