# ヤフーの主要トピックスを取得する

import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from time import sleep

url = 'https://www.yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

main_toppicks = soup.select(
    '._2jjSS8r_I9Zd6O9NFJtDN- > ul > li'
)

for main_toppick in main_toppicks:
    print(main_toppick.text)

# print(len(main_toppicks))
# print(main_toppicks.text)