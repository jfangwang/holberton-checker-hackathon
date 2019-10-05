#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, session
from checker import *
import re
import json
import time
import slack
app = Flask(__name__)

app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        api_key = request.form['api_key']
        session['api_key'] = api_key
        email = request.form['email']
        session['email'] = email
        password = request.form['usr_pwd']
        session['password'] = password
        user = get_auth_token(api_key, email, password)
        if not user:
            err = "Error: user information is not valid"
            return render_template('login.html', error=err)
        else:
            session['auth_token'] = user.get('auth_token')
            session['user_name'] = user.get('full_name')
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
            session['task_position'] = task_num
            rege = r"^(https://)?intranet\.hbtn\.io/projects/(\d+)$"
            match = re.search(rege, project)
            if not match or not task_num.isdigit():
                return render_template('project.html', error="Check format of project link and task!")
            else:
                project_id = match.group(2)
                project_j = get_project(project_id, session['auth_token'])
                session['project_name'] = project_j.get('name')
                try:
                    task = project_j.get('tasks')[int(task_num)]
                    task_id = task.get('id')
                    try_post = request_correction(task_id, session['auth_token'])
                    task_corr_id = try_post.get('id')
                    get_results = get_correction_result(task_corr_id, session['auth_token'])
                    if get_results.get('delay'):
                        print('delay')
                        time.sleep(get_results.get('delay'))
                    while get_results.get('status') != "Done" and get_results.get('status') != "Fail":
                        time.sleep(3)
                        print('waiting for correction to complete...')
                        get_results = get_correction_result(task_corr_id, session['auth_token'])
                    checks = get_results.get('result_display').get('checks')
                    passed = 0
                    for check in checks:
                        if check.get('passed'):
                            passed += 1
                    big_dict = {}
                    big_dict['user_name'] = session['user_name']
                    big_dict['project_name'] = session['project_name']
                    big_dict['task_position'] = session['task_position']
                    big_dict['completed_checks'] = passed
                    big_dict['total_checks'] = len(checks)
                    slack.post_slack(big_dict)
                    return("Check out your slack channel!")
                    """ FINAL DICTIONARY HERE IN big_dict """
                except Exception:
                    return render_template('project.html', error="Are you sure this task exists?")
    else:
        return render_template('project.html')

if __name__ == "__main__":
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run()
