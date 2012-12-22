# coding: UTF-8

# while文の書き方
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
    print i
    i += 1
else:
    print "end" 