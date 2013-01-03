# coding: UTf-8

import urllib
from bs4 import BeautifulSoup

url = "http://www.google.co.jp"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# ソースを成型して表示
print soup.prettify().encode("utf_8")

# タイトルをタグを含めて取得
print soup.title

# タイトルの属性のみ取得
print soup.title.string

# タグの内容を取得
print soup.a
print soup.a["class"]

# すべてのタグをリストに取得
print soup.find_all("a")

for link in soup.find_all("a"):
    print link.get("href")
