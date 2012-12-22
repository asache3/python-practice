# coding: UTF-8

# for文の書き方
sum = 0
for i in [1, 3, 5, 7, 9]:
    sum += i
else:
    print sum

# continueで処理を先頭に戻す
sum = 0
for i in range(10):
    if i == 3:
        continue
    sum += i
else:
    print sum

# breakでループを終了させる
sum = 0
for i in range(10):
    if i == 3:
        break
    sum += i
else:
    print sum # 表示されない

# for文で辞書型を使う
a = {"Tom":300, "Bob":500, "Emily":100}
for k, v in a.iteritems():
    print "Key: %s, Value: %d" % (k, v)

for k in a.iterkeys():
    print "Key: %s" % k

for v in a.itervalues():
    print "Value: %d" % v