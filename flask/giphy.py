import requests
import random


def get_giphy(search):
    params = {
        'api_key': '0i82h54aF0m2Gxz68XB4H0x7lc3EI4Nd',
        'q': search,
        'limit': 50
    }
    url = 'http://api.giphy.com/v1/gifs/search'
    res = requests.get(url, params=params)
    num = random.choice(range(50))
    return(res.json()['data'][num]['images']['downsized']['url'])
