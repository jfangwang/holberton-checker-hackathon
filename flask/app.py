#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, session
from checker import *
import re
import time
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        api_key = request.form['api_key']
        email = request.form['email']
        password = request.form['usr_pwd']
        user = get_auth_token(api_key, email, password)
        if not user:
            err = "Error: user information is not valid"
            return render_template('login.html', error=err)
        else:
            session['auth_token'] = user
            return redirect('/project')
    else:
        return render_template('login.html')

@app.route('/project', methods=['POST', 'GET'])
def project():
    if session.get('auth_token') is None:
        redirect('login.html')
    if request.method == 'POST':
            project = request.form['project']
            task_num = request.form['task_num']
            rege = r"^(https://)?intranet\.hbtn\.io/projects/(\d+)$"
            match = re.search(rege, project)
            if not match or not task_num.isdigit():
                return render_template('project.html', error="Check format of project link and task!")
            else:
                project_id = match.group(2)
                project_j = get_project(project_id, session['auth_token'])
                try:
                    task = project_j.get('tasks')[int(task_num)]
                    task_id = task.get('id')
                    try_post = request_correction(task_id, session['auth_token'])
                    get_results = get_correction_result(task_id, session['auth_token'])
                    while get_results.get('status') not in ["Done", "Fail"]:
                        time.sleep(1)
                        get_results = get_correction_result(task_id, session['auth_token'])
                    return get_results.get('result_display')
                except Exception:
                    return render_template('project.html', error="Are you sure this task exists?")
    else:
        return render_template('project.html')

if __name__ == "__main__":
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run()