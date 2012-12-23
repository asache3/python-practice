# coding: UTF-8

# 関数の作り方
def hello(name, num = 3):
    return "Hello %s. " % name * num

print hello("Tom", 2)
print hello("Bob")

# 関数で引数リストを受け取る
def foo(a, b, *vals):
    print a, b, vals

foo(1, 2, 3, 4, 5)

# 関数でキーワード引数を受け取る
def bar(a, b, **args):
    print a, b, args

bar (1, 2, c=3, d=4)

# 空の関数を定義する
def vacant():
    pass

# リストに関数を適用する
def double(x):
    return x * x

print map(double, [1, 2, 5])

# 無名関数を定義する
print map(lambda x:x * x, [1, 2, 5])