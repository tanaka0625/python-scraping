from oauth2client.service_account import ServiceAccountCredentials
import gspread

folder_id = '1dATyJ6wK3jpw3_otIGVY6VnNpoiGWc0h'
file_name = 'GC_test_by_gspread'

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Credentials 情報を取得
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    './key.json',
    scopes=scopes
)


# Auth2のクレデンシャルを使用してGoogleAPIにログイン
gc = gspread.authorize(credentials)

# スプレッドシートの新規作成
sh = gc.create(file_name, folder_id)
