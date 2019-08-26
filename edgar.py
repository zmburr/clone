from bs4 import BeautifulSoup
import requests
import re
import pickle
import feedparser
from time import sleep

#open file with stored item dictionary
# with open('file_name.pickle','wb') as handle:
#     pickle.dump(items_dict,handle,protocol=pickle.HIGHEST_PROTOCOL)
with open('file_name.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

locations = []
url = 'https://www.sec.gov/Archives/edgar/data/51143/000155837019006914/ibm-20190802x8k.htm'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
new = re.sub(r'\s+'," ",soup.text)
#dictionary turning keys item 7 to values text

item7 = re.search(r'Item 7\.01\. Regulation FD Disclosure.?',new).span()[0]
item9 = re.search(r'Item 9\.01\. Financial Statements and Exhibits', new).span()[0]
signature = re.search(r'SIGNATURE',new).span()[0]
#regFD = re.findall(r'Item\s\d\.\d\d\..*',new)
locations.append(item7)
locations.append(item9)
locations.append(signature)
for i in range(2):
    start = locations[i]
    end = locations[i + 1]
   # print(new[start:end])



print(unserialized_data)