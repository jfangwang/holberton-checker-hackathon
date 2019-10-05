import requests
import json
from random import randrange, choice
import giphy


def set_msg(_dict):
    gif_search = ["amazing", "way to go", "keep going", "great job", "kudos", "you're awesome"]
    if (_dict['completed_checks'] < (_dict['total_checks'] / 2) - 1):
        message = {
                        "text": msgs(0, _dict),
                        "attachments": [
                            {
                                "fallback": "Required plain-text summary of the attachment.",
                                "title": "Checker Daddy",
                                "author_icon": "https://img.icons8.com/cotton/64/000000/checkmark.png",
                                "image_url": giphy.get_giphy(choice(gif_search))
                            }
                        ]
                    }
    elif _dict['completed_checks'] != _dict['total_checks'] and _dict['completed_checks'] >= (_dict['total_checks'] / 2):
        message = {
                        "text": msgs(1, _dict),
                        "attachments": [
                            {
                                "fallback": "Required plain-text summary of the attachment.",
                                "title": "Checker Daddy",
                                "author_icon": "https://img.icons8.com/cotton/64/000000/checkmark.png",
                                "image_url": giphy.get_giphy(choice(gif_search))
                            }
                        ]
                    }
    else:
        message = {
                        "text": msgs(2, _dict),
                        "attachments": [
                            {
                                "fallback": "Required plain-text summary of the attachment.",
                                "title": "Checker Daddy",
                                "author_icon": "https://img.icons8.com/cotton/64/000000/checkmark.png",
                                "image_url": giphy.get_giphy(choice(gif_search))
                            }
                        ]
                    }
    return message


def post_slack(_dict):
    data = json.dumps(set_msg(_dict))

    url = 'https://hooks.slack.com/services/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'
    result = requests.post(url, data=data)


def msgs(val, _dict):
    '''
    _dict = {
                "user_name": "Joe",
                "project_name": "Monty",
                "task_name": "FizzBuzz",
                "completed_checks": 5,
                "total_checks": 8
            }
    '''
    _dict["task_name"] = "FizzBuzz"

    if val == 0:
        under_half = ["{} / {} checks on {}: This is the start of a new adventure {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: You're gonna get there {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: The love of Betsy is so much bigger than the size of the problem you have {}, pray!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: {}, you can do anything, I believe in you!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: The pain you feel today will be the strength you feel tomorrow {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: {}, start by doing what's necessary, then do what's possible, and suddenly you're doing the impossible!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: {}, the greatest accomplishment is not in never falling but in rising again after you fall!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: {}, sometimes when you're in a dark place, you think you've been buried, but actually you've been planted!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"])]
        message = under_half[randrange(len(under_half))]

    elif val == 1:
        over_half = ["{} / {} checks on {}: {}, you are smarter than you think!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: Get that checker money {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: Fight for your dreams {}, never let anyone break you down by saying that you can't do something!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: {}, you are doing a great job!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: Make Betsy proud {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: You got this {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: {}, green checks are life's ways of saying that there is a bright future in store for you!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                      "{} / {} checks on {}: Trusty Betsy's plan {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"])]
        message = over_half[randrange(len(over_half))]

    else:
        done = ["{} / {} checks on {}: {}, green checker money baby!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: You deserve nothing but the best {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: Go help your peers {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: {}, did you do all the advanced?".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: Go home {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: Go to bed {}".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: {} you believed in yourself and you made it!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: {}, May you forever be as happy as your are today!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"]),
                "{} / {} checks on {}: Your dedication towards work is really inspiring {}!".format(_dict["completed_checks"], _dict["total_checks"], _dict["task_name"], _dict["user_name"])]
        message = done[randrange(len(done))]
    return message
