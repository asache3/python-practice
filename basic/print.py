# coding: UTF-8

# 文字列を表示
print "Hello Python!"

# 日本語を表示
print u"こんにちは、パイソン！"

# 桁数を固定して表示
a = 10
print "My age is %05d." % a

# 複数の変数を表示
b = "Tom"
print "%s is %d years old." % (b, a)

# 辞書の内容を表示
c = {"Bob":50, "Emily":30}
print "%(Bob)d" % c