# coding: UTF-8

# リストの作り方
a = [1, 3, 5, 7, 9]
print range(10)
print range(3, 10)
print range(3, 10, 2)

# 要素の置き換え
a[2] = "Five"
print a

# 要素の削除
del a[4]
a.remove(1)
print a

# 末尾に要素を追加する
a.append(11)
print a

# リストに要素を追加する
a.insert(1, 13)
print a

# 要素を1つだけ取り除く
print a.pop()
print a.pop(0)

# 要素の存在チェック
print 7 in a

# リストの最大値、最小値
price = [300, 120, 500, 1000, 750]
print max(price)
print min(price)

# リストのソート
price.sort()
print price

# リストの順序の反転
price.reverse()
print price

# 文字列をリストに分割する
date = "2012/12/22"
print date.split("/")

# リストを文字列に連結する
s = ["a", "b", "c"]
print "-".join(s)