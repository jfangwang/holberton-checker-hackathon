#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
@app.route('/')
def login():
    return render_template('login.html', user='Ethan')
