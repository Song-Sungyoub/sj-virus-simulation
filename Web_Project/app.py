import sqlite3
from flask import Flask, url_for, render_template, Request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()