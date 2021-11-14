from flask import Flask, render_template
from gphotospy import authorize
from gphotospy.album import *


app = Flask(__name__)
CLIENT_SECRET_FILE = "./gphoto_oauth.json"
service = authorize.init(CLIENT_SECRET_FILE)

@app.route('/')
def hello():
    return render_template('index.html')