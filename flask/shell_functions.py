#!/usr/bin/python3
"""Provide functions supporting the shell"""
import json
import os
import re
from getpass import getpass
from sys import argv
from os.path import expanduser

home = expanduser("~")
cred_dir = home + "/.hbchecker.json"


def intro():
    """Shows the intro on first boot"""
    welcome = ("\nWelcome to HBChecker 2.0! In version 2.0, we use the"
               " Holberton API to fetch and query results. This project was"
               " created so you can run the checker without clicking the "
               "'Check code button' everytime. To use this program, you will"
               " enter holberton credentials and API key which will be saved "
               " in '"+cred_dir+"'."
               ".\n\nType 'man hbchecker' for more information.")
    print(welcome)


def get_user():
    """Gets the username"""
    tries = 0
    email = "@holbertonschool.com"
    username = input("Holberton email: ")
    while email not in username and tries <= 1:
        print("Email not recognized, try again")
        username = input("Holberton email: ")
        tries += 1
    if email not in username:
        print("Exiting script, email did not end in '@holbertonschool.com'.")
        exit()
    return username


def get_pass():
    """Gets the password"""
    tries = 0
    pass1 = "Pass1"
    pass2 = "Pass2"
    while pass1 != pass2 and tries <= 2:
        tries += 1
        pass1 = getpass("Holberton password: ")
        pass2 = getpass("Re-enter password: ")
        if pass1 != pass2:
            print("Passwords did not match, try again")
    if tries > 2:
        print("You attempted 3 times and decided to end the program.")
        exit()
    return pass1


def get_key():
    """Gets the API Key"""
    advance = "n"
    tries = 0
    while advance == "n" and tries <= 2:
        api_key = input("Enter your API Key: ")
        advance = input("You entered: "+api_key+". Is this correct? (y/n): ")
        if "n" in advance:
            print("Asking you again...")
        tries += 1
    if tries > 2:
        print("You said no 3 times, please start again.")
        exit()
    return api_key


def get_proj(link=None):
    """Gets the project link"""
    rege = r"^(https://)?intranet\.hbtn\.io/projects/(\d+)$"
    if link is None:
        link = input("Enter the project link or number: ")
    if link.isdigit():
        return link
    else:
        match = re.search(rege, link)
        if not match:
            print("Check format of project link and task!")
        else:
            return match.group(2)
        
    print("Link was not valid, please start again.")
    exit()

    if tries > 2:
        print("You said no 3 times, please start again.")
        exit()
    return api_key


def save(user, password, key, proj):
    """Saves the credentials in /etc/hbchecker.txt"""
    cred = {
            "user": user,
            "pass": password,
            "key": key,
            "proj": proj
            }
    with open(cred_dir, 'w') as f:
        json.dump(cred, f)


def get_cred():
    """Gets the user's credentials regardless if it's their first
       time or not"""
    if os.path.isfile(cred_dir) is False:
        intro()
    try:
        with open(cred_dir, 'r') as f:
            loaded_dict = json.load(f)
            """Get User"""
            if loaded_dict["user"] is None:
                user = get_user()
                if user is None:
                    return
            else:
                user = loaded_dict["user"]
            """Get Password"""
            if loaded_dict["pass"] is None:
                password = get_pass()
                if password is None:
                    return
            else:
                password = loaded_dict["pass"]
            """Get API Key"""
            if loaded_dict["key"] is None:
                key = get_key()
                if key is None:
                    return
            else:
                key = loaded_dict["key"]
            """Get Proj"""
            if loaded_dict["proj"] is None:
                proj = get_proj()
                if proj is None:
                    return
            else:
                proj = loaded_dict["proj"]
            cred = {
                "user": user,
                "pass": password,
                "key": key,
                "proj": proj
            }
            return cred
    except:
        """Get User"""
        user = get_user()
        if user is None:
            return
        """Get Password"""
        password = get_pass()
        if password is None:
            return
        """Get API Key"""
        key = get_key()
        if key is None:
            return
        """Get Proj"""
        proj = get_proj()
        if proj is None:
            return
        cred = {
            "user": user,
            "pass": password,
            "key": key,
            "proj": proj
        }
        return cred

def get_files_changed():
    """Gets which files were changed"""
    files_list = []
    test = os.popen('git show --name-only')
    repo_location = os.popen('git rev-parse --show-toplevel')
    repo_location = repo_location.readlines()
    repo_location = repo_location[0]
    repo_location = repo_location.replace('\n', '')
    if "Not a git repository" in repo_location:
        files_list.append("Not a git repository")
        return files_list
    files_list.append(repo_location.split('/')[-1])
    output = test.readlines()
    for a in range(6, len(output)):
        files_list.append(output[a].replace('\n', ''))
    return files_list