# ヤフーの主要トピックスのタイトルとリンクを取得して辞書にする

import requests
from bs4 import BeautifulSoup


# urlの例 'https://www.yahoo.co.jp/'
# selectorの例　'._2jjSS8r_I9Zd6O9NFJtDN- > ul > li > article > a'
def do(url: str, selector: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    main_toppicks = soup.select(selector)

    # タイトルとリンクと番号をまとめた辞書が入った配列を作成
    main_toppicks_dics = []
    for i in range(0, len(main_toppicks)):

        # トピック一つの情報が入った辞書を作成
        # 2行目以降
        if(i==0):
            main_toppick_dic = [
                "No",
                "タイトル",
                "リンク"    
            ]
        # 1行目
        elif(i>0):
            main_toppick_dic = [
                i+1,
                main_toppicks[i].text,
                main_toppicks[i]["href"]    
            ]

        # 辞書をまとめる
        main_toppicks_dics.append(main_toppick_dic)

    return main_toppicks_dics