# coding:utf-8

# adding bark key here for notification
# CAUTION !!! do NOT upload keys to GitHub
import requests
from requests.utils import requote_uri

server_chain_key = ''
bark_key = ''


def bark(title, content, bark_key=bark_key):
    url = requote_uri("https://api.day.app/{}/{}/{}".format(bark_key, title, content))
    return requests.get(url).content


def pushover(title, content, user=pushover_user, token=pushover_token):
    url = "https://api.pushover.net/1/messages.json"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    json_data = json.dumps({
        "message": content,
        "device": "guoph-iPhone",
        "title": title,
        "token": token,
        "user": user
    })
    if SEND_NOTIFICATION:
        try:
            return requests.post(url=url, headers=headers, data=json_data).content
        except:
            raise Exception("Sent notification failed.")
    else:
        print(title, content)


def main():
    title = "Test"
    content = "Test"
    bark(title, content)


if __name__ == '__main__':
    main()
