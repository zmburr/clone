import requests
import json
import re
from urllib.parse import urljoin

front_link = 'https://www.blog.google'
url = 'https://www.blog.google/api/v2/latest/?author_ids=&category=&date_start=&date_stop=&paginate=7&tags=&template=latestArticleItem'
data = requests.get(url)
letters = json.loads(data.text)
headlines = []
count = 0


for each in letters.values():
    for key in each:
        if len(key) >1:
            for i in key.keys():
                if i == 'url':
                    link = urljoin(front_link,key[i])
                    if count == 0:
                        headlines.append(link)
                    else:
                        if link not in headlines:
                            print(link)
                            headlines.append(link)

print(headlines)
    # if each.keys() == 'url':
    #     print(each.keys())
        # link_start = re.search(r'/inspections-',dict[each]).span()[0]
        # link_end = re.search(r'">',dict[each]).span()[0]
        # print(each['url'])
        # link = urljoin(front_link, url)
        # print(link)
        # if count == 0:
        #     headlines.append(link)
        # else:
        #     if link not in headlines:
        #         print(link)
        #         headlines.append(link)



