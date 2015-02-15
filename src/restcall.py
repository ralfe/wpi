__author__ = 'renderle'

import requests
import json


def doReq(url, data):
    response = requests.get(url, params=data)
    print(response)
    data = response.json()

    #print("----> 2: WeatherData response")
    #print("URL :", response.url)
    #print("status code: ", response.status_code)
    #print("data ", data)

    return data
