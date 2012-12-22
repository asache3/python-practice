# coding: UTF-8

# セットの作り方
s1 = set(["a", "b", "c"])
s2 = set(["a", "b", "d"])

# s1にあってs2にないものを表示
print s1 - s2

# 和集合を表示
print s1 | s2

# 積集合を表示
print s1 & s2

# どちらかにしかないものを表示
print s1 ^ s2