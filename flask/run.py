#!/usr/bin/python3
from flask import Flask, render_template, request
from checker import *
app = Flask(__name__)

@app.route('/login')
@app.route('/')
def login():
    return render_template('login.html', user='Ethan')

@app.route('/check_login', methods=['POST'])
def check_login():
    api_key = request.form['api_key']
    email = request.form['email']
    password = request.form['password']
    return get_user_profile(get_auth_token(api_key, email, password))
