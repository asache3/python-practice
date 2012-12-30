# coding: UTF-8

import urllib

file = urllib.urlopen("http://www.yahoo.co.jp/")

# Proxyを通す場合
# proxyUrl = {'http':'http://<proxyserver>:<port>'}
# file = urllib.urlopen("http://www.yahoo.co.jp/", proxies = proxyUrl)

# データを文字列として返す
print file.read()

# データから1行だけ読み込む
file = urllib.urlopen("http://www.google.co.jp/")
print file.readline()

# 各行をリストにして読み込む
print file.readlines()

# 取得したURLを返す
print file.geturl()