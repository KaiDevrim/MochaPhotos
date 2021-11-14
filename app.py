from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("app.db")
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    likes = c.execute('SELECT likes FROM Photos').fetchall()
    return render_template('index.html', imgs=os.listdir('./static/photos'), likes=likes)

@app.route('/like/<image>',methods = ['GET','POST'])
def like(image):
    print(image)
    conn = sqlite3.connect('./app.db')
    conn.execute("UPDATE Photos SET LIKES = LIKES {} 1 WHERE PATH = '{}'".format('+',image))
    conn.commit()
    conn.close()
    return(image)