# ヤフーの主要トピックスのタイトルとリンクを取得して辞書にする

import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from time import sleep

url = 'https://www.yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

main_toppicks = soup.select(
    '._2jjSS8r_I9Zd6O9NFJtDN- > ul > li > article > a'
)

# タイトルとリンクと番号をまとめた辞書が入った配列を作成
main_toppicks_dics = []
for i in range(0, len(main_toppicks)):

    # トピック一つの情報が入った辞書を作成
    main_toppick_dic = {
        "No":i+1,
        "title":main_toppicks[i].text,
        "link":main_toppicks[i]["href"]    
    }

    # 辞書をまとめる
    main_toppicks_dics.append(main_toppick_dic)

print(main_toppicks_dics)