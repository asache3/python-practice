# coding: UTF-8

import os

# oSの名前
print os.name

# 環境変数
print os.environ

# 現在の作業ディレクトリ
print os.getcwd()

# 作業ディレクトリを変更
os.chdir("C:\\")
print os.getcwd()

# ディレクトリ内のエントリを表示
print os.listdir(os.getcwd())

# ディレクトリを作成する
os.mkdir("sample")

# ディレクトリが存在するかを調べる
print os.path.isdir("sample")

# ディレクトリを削除する
os.rmdir("sample")
print os.path.isdir("sample")

