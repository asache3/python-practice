# coding: UTF-8

# ファイルオブジェクトを作る
f = open("foo.txt", "r")
s = f.read()
f.close()

# ファイルから1行ずつ読み込む
f = open("foo.txt", "r")
for line in f:
    print line
f.close()

# ファイルに書き込む
s = "hoge"
f = open("newfile.txt", "w")
f.write(s)
f.close()