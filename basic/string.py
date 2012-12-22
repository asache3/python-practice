# coding: UTF-8

# 改行を含んだ文字列や長い文字列を定義する
print """<body>
<h2>Page Title</h2>
<p>
Page body.
</p>
</body>"""

# 文字列の繰り返し
print "ムダ！" * 10

# 文字列の長さを取得する
print len("abcdefg")

# 文字列を切り出す
s = "hijklmn"
print s[1]
print s[1:5]
print s[1:]
print s[:5]
print s[1:-1]

# 文字列の検索
print s.find("jk")
print s.find("jp")

# 文字列の置換
print s.replace("mn", "mmnn")

# 文字列から数値への変換
print 3 + int("10")
print 5 + float("2.0")

# 数値から文字列への変換
age = 30
print "I am " + str(age) + " years old."
