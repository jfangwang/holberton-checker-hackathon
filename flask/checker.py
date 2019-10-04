#!/bin/usr/env python3
''' Define functions for retrieving data from the Holberton Checker API. '''
import requests
import json


def get_auth_token(api_key=Config['api_key'],
                   email=Config['email'],
                   password=Config['password'],
                   scope='checker'):
    ''' Get auth token for API use.

        Args:
            api_key - User's API key.
            email - User's Holberton email.
            password - User's password.
            scope - Scope of API usage.

        Make POST request to the `/users/auth_token.json` endpoint of the API
        with api_key, email, password, and scope as parameters.

        Return: Auth token from response as a string.
    '''
    params = {
        "api_key": api_key,
        "email": email,
        "password": password,
        "scope": scope
        }
    url = "https://intranet.hbtn.io/users/auth_token.json"
    result = requests.post(url, params=params)
    json_ = (result.json())
    return(json_['auth_token'])


def get_user_profile(auth_token=get_auth_token()):
    ''' Return JSON representation of a user. '''
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/users/me.json'
    result = requests.get(url, params=params)
    return(result.json())


def get_project(project_id, auth_token=get_auth_token(),):
    ''' Return JSON representation of a project.

        Args:
            project_id - The ID of a project as a string. Can be found on the
            "Projects" page of the intranet next to the project's name.
    '''
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/projects/{}.json'.format(project_id)
    result = requests.get(url, params=params)
    return(result.json())


def get_tasks(task_id, auth_token=get_auth_token()):
    ''' Return JSON representation of the task with the given ID. '''
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/tasks/{}.json'.format(task_id)
    result = requests.get(url, params=params)
    return(result.json())


def request_correction(task_id, auth_token=get_auth_token()):
    ''' Request a correction for the task with the given ID. '''
    params = {'auth_token': auth_token}
    url = 'https://intranet.hbtn.io/tasks/{}/start_correction.json'.format(
            task_id)
    result = requests.post(url, params=params)
    return(result.json())


def get_correction_result(correction_id, auth_token=get_auth_token()):
    ''' Get the JSON representation of a correction result given the
    correction's ID. '''
    params = {'auth_token': get_auth_token}
    url = 'https://intranet.hbtn.io/correction_requests/{}.json'.format(
            correction_id)
    result = requests.get(url, params=params)
    return(result.json())
