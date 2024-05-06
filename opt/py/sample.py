# ヤフーのh1タグを取得する

import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from time import sleep

url = 'https://www.yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
for h1 in soup.find_all('h1'):
    print(h1)