# coding: utf8
from .. import db
from ..models import Caption
from . import main
import requests, urllib3
from bs4 import BeautifulSoup
from dateutil import parser
import re

def parseM():
    url = 'https://meduza.io/rss/all'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
            }
    r = requests.get(url, headers = headers)

    soup = BeautifulSoup(r.text, "xml")
    allPosts = soup.select('item')

    db.create_all()

    for i in range(len(allPosts)):
        mLink = (re.sub('^\s+|\n|\r|\s+$', '', allPosts[i].link.string))
        mTopic = (re.sub('^\s+|\n|\r|\s+$', '', allPosts[i].title.string))
        mTime = parser.parse(re.sub('^\s+|\n|\r|\s+$', '', allPosts[i].pubDate.string))
        mText = (re.sub('^\s+|\n|\r|\s+$', '', allPosts[i].description.string))

        newItem = Caption(c_link = mLink, c_topic = mTopic,
                          c_text = mText, c_time = mTime,
                          source = Caption.query[0].source)
        db.session.add(newItem)

    db.session.commit()
