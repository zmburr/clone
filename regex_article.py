import feedparser
import requests
import re

link = 'https://newsroom.fb.com/feed/'

d = feedparser.parse(link)

for entry in d.entries:

    print(entry.title)