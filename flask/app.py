#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
from checker import *
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        api_key = request.form['api_key']
        email = request.form['email']
        password = request.form['user_pwd']
        user = get_user_profile(get_auth_token(api_key, email, password))
        if not user:
            return "ERROR"
        else:
            return redirect('/project')
    else:
        return render_template('login.html')

@app.route('/project', methods=['POST', 'GET'])
def project():
    if request.method == 'POST':
            project = request.form['project']
            