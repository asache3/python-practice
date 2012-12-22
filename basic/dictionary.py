# coding: UTF-8

# 辞書の作り方
d = {"name": "Guido", "nickname": "GvR"}
print d["name"]

# 要素を追加する
d['birthyear'] = 1964
print d

# 要素を削除する
del d["nickname"]
print d

# キーと値の一覧を取得する
print d.keys()
print d.values()

# キーと値をタプルのリストで返す
print d.items()

# キーの存在チェック
print "name" in d
print d.has_key("age")