# coding:utf-8
# adding bark key here for notification
# CAUTION: do NOT upload keys to GitHub
import os
import requests
from requests.utils import requote_uri

from keys import bark_key, pushover_token, pushover_user, pushover_device, sudo_password
import json


def shutdown():
    cmd = "shutdown -h now"
    os.system("echo {}|sudo -S {}".format(sudo_password, cmd))


def bark(title, content, bark_key=bark_key):
    url = requote_uri("https://api.day.app/{}/{}/{}".format(bark_key, title, content))
    return requests.get(url).content


def pushover(title, content):
    url = "https://api.pushover.net/1/messages.json"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    json_data = json.dumps({
        "message": content,
        "device": pushover_device,
        "title": title,
        "token": pushover_token,
        "user": pushover_user
    })
    return requests.post(url=url, headers=headers, data=json_data).content


if __name__ == '__main__':
    title = "Test"
    content = "Test"
    pushover(title, content)
    bark(title, content)
