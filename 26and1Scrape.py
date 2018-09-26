# -*- coding: utf-8 -*-
"""
参考URL: https://qiita.com/Yukiya025/items/c80b143427ceaa343c22
yakuru.net: https://yakuru.net/search.aspx?w=%D1%8D%D1%82%D0%BE
辞書をスクレイピングするために書いたコード
"""
from bs4 import BeautifulSoup
import requests
import csv

# солдат の日本語訳頁
r = requests.get("https://translate.google.co.jp/?hl=ja#ru/ja/%D1%81%D0%BE%D0%BB%D0%B4%D0%B0%D1%82")
soup_content = BeautifulSoup(r.content, "html.parser")

ru_txt = str(soup_content.prettify)
with open('yakuru.html', 'w+', encoding = 'utf-8') as f:
    # write()の引数は必ず文字列
    f.write(ru_txt)
pass
