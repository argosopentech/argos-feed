from content import *

from bs4 import BeautifulSoup
from urllib import request, parse


def parse_rss(feed):
    headers = {"user-agent": "argos-feed", "accept": "*/*"}
    req = request.Request(str(feed), headers=headers)
    res = request.urlopen(req).read()
    soup = BeautifulSoup(res, "xml")
    channels = soup.find_all("channel")
    if len(channels) < 1:
        return list()
    channel = channels[0]
    items = channel.find_all("item")
    to_return = list()
    for item in items:
        content = Content()
        content.title = item.title.text
        content.link = item.link.text
        to_return.append(content)
    return to_return


def download():
    feed_urls = [
        "https://feeds.feedblitz.com/marginalrevolution",
        "https://astralcodexten.substack.com/feed",
    ]
    feeds = [parse_rss(feed_url) for feed_url in feed_urls]
    return feeds


feeds = download()
for feed in feeds:
    for content in feed:
        print(content)
