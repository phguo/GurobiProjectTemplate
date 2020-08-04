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


def main():
    title = "Test"
    content = "Test"
    bark(title, content)


if __name__ == '__main__':
    main()
