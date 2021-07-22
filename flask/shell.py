#!/usr/bin/python3
from checker import *
from shell_functions import *


def run_shell():
    """This will run the shell and be incorporated with git commands"""
    credentials = get_cred()
    user = credentials["user"]
    password = credentials["pass"]
    key = credentials["key"]
    proj = credentials["proj"]
    for index in range(1, len(argv)):
        if "https://intranet.hbtn.io/projects" in argv[index] or \
        argv[index].isdecimal():
            proj = get_proj(argv[index])

    save(user, password, key, proj)
    
    """Get Authentication"""
    account_json = get_auth_token(key, user, password)
    if not account_json:
        print("Error: user information is not valid")
        return
    full_name = account_json["full_name"]
    auth_token = account_json["auth_token"]
    print("\nWelcome " + full_name + "! ")
    
    """Get Project"""
    project_json = get_project(proj, auth_token)
    # print(project_json)
    project_name = project_json["name"]
    project_tasks = project_json["tasks"]
    print("You have selected to check " + project_name +
    ". This project has " + str(len(project_tasks)) + " tasks.\n")
    
    """Check tasks"""
    check_files = get_files_changed()
    for task in project_tasks:
        file_exists = False
        # for f in check_files:
        for f in task["github_file"]:
            if f in task["github_file"]:
                file_exists = True
                print("--------------------------")
                if task["checker_available"] is False:
                    print(str(task["position"]) + " is \033[5;30;43mMANUAL QA REVIEW\033[0m")
                else:
                    print(str(task["position"]) + " has a \033[5;30;42mCHECKER\033[0m")
                    # print(get_tasks(task["id"], auth_token))
                    # corr_id = request_correction(task["id"], auth_token)
                    # print(corr_id)
                    # print(get_correction_result(corr_id["id"], auth_token))
                break;
        if file_exists == False:
            pass
    print("--------------------------")
    return
run_shell()
    