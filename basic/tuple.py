# coding: UTF-8

# タプルの作成
a = (1, 3, 5, 7, 9)

# タプルからリストへの変換
b = list(a)
print b

# リストからタプルへの変換
c = tuple(b)
print c

# タプルは辞書のキーとして利用できる
ipmap = {(0, 1, 2, 3) : "host.name.com",
         (0, 2, 1, 3) : "some.dname.com"}