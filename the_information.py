from bs4 import BeautifulSoup
import requests
import lxml.html
from time import sleep
import twitter

url = 'https://www.theinformation.com/'
count = 0
headlines = []
def scrape_information():
    r = requests.get(url)
    root = lxml.html.fromstring(r.content)
    titles = root.xpath('//*[@id="home-page"]/div/div[2]/div[2]/div/div[2]/a')
    links = root.xpath('//*[@id="home-page"]/div/div[2]/div[2]/div/div[2]/a/@href')
    link = links[0]
    title = titles[0].text
    if count == 0:
        headlines.append(link)
    