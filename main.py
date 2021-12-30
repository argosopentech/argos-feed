from content import *

from bs4 import BeautifulSoup
from urllib import request, parse

def get_feed(feed):
    req = request.Request(str(feed))
    res = request.urlopen(req).read()
    soup = BeautifulSoup(res, 'xml')
    entries = soup.find_all('item')
    to_return = list()
    for entry in entries:
        content = Content()
        content.title = entry.title.text
        content.link = entry.link.text
        to_return.append(content)
    return to_return

def download():
    feed_urls = ['https://feeds.feedblitz.com/marginalrevolution']
    feeds = [get_feed(feed_url) for feed_url in feed_urls]
    return feeds

feeds = download()
for feed in feeds:
    for content in feed:
        print(content)
