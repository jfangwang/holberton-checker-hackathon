import requests
import json
from random import randrange


def post_slack():
    under_half = ["This is the start of a new adventure!", "Filler", "daddy", "betsy"]
    under_half = ["This is the start of a new adventure!", "Filler", "daddy", "betsy"]
    under_half = ["This is the start of a new adventure!", "Filler", "daddy", "betsy"]
    # if {completed_checks} < ({total_checks} / 2) - 1:
    if True:
        message = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                                    "type": "mrkdwn",
                                    "text": under_half[randrange(len(under_half))]
                                }
                    }
                    ]
                }
    elif {completed_checks} != {total_checks} and {completed_checks} >= {total_checks} / 2:
        message = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                                    "type": "mrkdwn",
                                    "text": "You'll get it!"
                                }
                    }
                    ]
                }
    else:
        message = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                                    "type": "mrkdwn",
                                    "text": "Almost there!"
                                }
                    }
                    ]
                }
    data = json.dumps(message)

    url = 'https://hooks.slack.com/services/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'
    result = requests.post(url, data=data)
    print(result.text)
    print(result.reason)



"""
    data = json.dumps({
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Danny Torrence left the following review for your property:"
      }
    },
    {
      "type": "section",
      "block_id": "section567",
      "text": {
        "type": "mrkdwn",
        "text": "<https://google.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
      },
      "accessory": {
        "type": "image",
        "image_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",
        "alt_text": "Haunted hotel image"
      }
    },
    {
      "type": "section",
      "block_id": "section789",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Average Rating*\n1.0"
        }
      ]
    }
  ]
})
"""
