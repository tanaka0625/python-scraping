# スプレッドシートを作成　ヤフートップニュースから取得した辞書書き込み

from selenium import webdriver 
from time import sleep
import gspread
import datetime

from functions import make_credentials
from functions import make_main_toppiks_dics


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

key_pass = "./key.json"

# credentials作成
credentials = make_credentials.do(scopes, key_pass)

# Auth2のクレデンシャルを使用してGoogleAPIにログイン
gc = gspread.authorize(credentials)

# スプレッドシートの新規作成
dt_now = datetime.datetime.now().strftime("%Y/%m/%d/ %H:%M:%S")
name = dt_now
ss = gc.create(name, "1dATyJ6wK3jpw3_otIGVY6VnNpoiGWc0h")

# シートを特定する（シートインデックスで特定）
st = ss.get_worksheet(0) #0は左から1番目のシート

# シート名変更
st_name = "主要トピックス"
st.update_title(st_name)

# 辞書作成
url = 'https://www.yahoo.co.jp/'
selector = '._2jjSS8r_I9Zd6O9NFJtDN- > ul > li > article > a'
main_toppicks_dics = make_main_toppiks_dics.do(url, selector)

# 書き込み
st.append_rows(values=main_toppicks_dics, table_range='B2')