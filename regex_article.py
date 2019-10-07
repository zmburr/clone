import feedparser
import requests
import re
import flashtext
from newspaper import Article

source = 'ABC News'
link = 'https://abcnews.go.com/Business/gm-union-reach-deal-end-strike-weekend-sources/story?id=65875346'
    #''
keywords = ['sources added','source familiar','spokesperson told', 'source close to the situation said','has learned','according to one source']
processor = flashtext.KeywordProcessor()
processor.add_keywords_from_list(keywords)

def parse_text(link):
    locations = []
    text_list = []
    keywords_found = []
    article = Article(link)
    article.download()
    article.parse()
    text = article.text.lower()
    found = processor.extract_keywords(text)
    if len(found) > 0:
        keywords_found = [word for word in found]
    for key in keywords_found:
        search = re.search(key,text)
        if search:
            locations.append(search.span()[1])
        for i in range(len(locations) - 1):
            start = 0
            end = locations[i + 1]
            text_list.append((text[start:end]))
    for x in range(len(text_list) - 1):
        each = text_list[x]
        print(each)
    print(locations)

parse_text(link)



