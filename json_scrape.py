import requests
import json
import re
from urllib.parse import urljoin

front_link = 'https://www.fda.gov'
url = 'https://www.fda.gov/files/api/datatables/static/warning-letters.json?_=1568318768661'
data = requests.get(url)
letters = json.loads(data.text)
headlines = []
count = 0

for dict in letters:
    for each in dict.keys():
        if each == 'field_company_name_warning_lette':
            link_start = re.search(r'/inspections-',dict[each]).span()[0]
            link_end = re.search(r'">',dict[each]).span()[0]
           #print(dict[each][link_start:link_end])
            link = urljoin(front_link,dict[each][link_start:link_end])
            if count == 0:
                headlines.append(link)
            else:
                if link not in headlines:
                    print(link)
                    headlines.append(link)


