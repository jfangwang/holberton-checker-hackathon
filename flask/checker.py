#!/bin/usr/env python3
import requests
import json

def get_auth_token(api_key,
                   email,
                   password,
                   scope='checker'):
    params = {
        "api_key": api_key,
        "email": email,
        "password": password,
        "scope": scope
        }
    url = "https://intranet.hbtn.io/users/auth_token.json"
    result = requests.post(url, params=params)
    json_ = (result.json())
    if json_.get('error'):
        return None
    return json_['auth_token']

def get_user_profile(auth_token):
    if not auth_token:
        return None
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/users/me.json'
    result = requests.get(url, params=params)
    return(result.json())

def get_project (project_id, auth_token):
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/projects/{}.json'.format(project_id)
    result = requests.get(url, params=params)
    return(result.json())

def get_tasks(task_id, auth_token):
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/tasks/{}.json'.format(task_id)
    result = requests.get(url, params=params)
    return(result.json())

def request_correction(task_id, auth_token):
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/tasks/{}/start_correction.json'.format(task_id)
    result = requests.post(url, params=params)
    return(result.json())

def get_correction_result(correction_id, auth_token):
    params = {'auth_token': get_auth_token}
    url = 'https://intranet.hbtn.io/correction_requests/{}.json'.format(correction_id)
    result = requests.get(url, params=params)
    return(result.json())
