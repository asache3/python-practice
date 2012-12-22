# coding: UTF-8

# if文の書き方
score = 70
if score > 80:
    print "Good"
elif score > 60:
    print "So So"
else:
    print "Too bad"

if 60 < score < 80:
    print "B"

# 1行で書く
print "Pass!" if score >= 80 else "Not pass..."