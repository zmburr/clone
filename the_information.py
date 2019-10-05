from bs4 import BeautifulSoup
import requests
import lxml.html
import tweepy
import urllib
from time import sleep

url = 'https://www.theinformation.com/'
count = 0
headlines = []

access_token = '68510437-HOiWOfkWLfaULGKN1C3su9vF7rnF0aVY0qV0IfvPJ'
access_secret = 'CvpCN351xJeLBmj8WfDgS6XrM5cfwGuWlVY0PeLnpUVpS'
consumer_key = 'PEp9dLKoIrlCE03GB7oNIXmhz'
consumer_secret = 'L9IjdP0MrIdeFUdab0bfDYUAnhh7IP582BnE9owwnpW3iApd9R'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
api = tweepy.API(auth)
r = requests.get(url,headers=headers)
print(r)
soup = BeautifulSoup(r.text,'html.parser')
articles = soup.find_all('a')
print(articles)
