# coding: UTF-8

# 関数の作り方
def hello(name, num = 3):
    return "Hello %s. " % name * num

print hello("Tom", 2)
print hello("Bob")

# 空の関数を定義する
def vacant():
    pass

# リストに関数を適用する
def double(x):
    return x * x

print map(double, [1, 2, 5])

# 無名関数を定義する
print map(lambda x:x * x, [1, 2, 5])