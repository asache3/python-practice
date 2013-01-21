# coding: UTF-8
import sys

from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure

# Connectionオブジェクトを作る
try:
    c = Connection(host="localhost", port=27017)
    print "Connected successfully"
except ConnectionFailure, e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)

# Database Handleを取得する
dbh = c["mydb"]

user_doc = {
    "username" : "janedoe",
    "firstname" : "Jane",
    "surname" : "Doe",
    "dateofbirth" : datetime(1974, 4, 12),
    "email" : "janedoe74@example.com",
    "score" : 0
}

dbh.users.insert(user_doc, safe=True)
print "Successfully inserted document %s" % user_doc

# Replica Setの中の少なくとも2つのサーバーに書き込む
dbh.users.insert(user_doc, w=2)

# 条件に合ったものを1つだけ検索する
dbh.users.find_one({"username":"janedoe"})

# 条件に合ったものをすべて検索する
dbh.users.find({"firsename":"jane"})
for user in users:
    print user.get("email")

# 条件に合ったものから特定の値を抽出する
dbh.users.find({"firstname":"jane"}, {"email":1})

# 条件に合うものの件数を取得する
userscount = dbh.users.find().count()
print "There are %d documents in users collection" % userscount

# 検索した結果をソートする
dbh.users.find({"firstname":"jane"}).sort(("dateofbirth", pymongo.DESCENDING))
users = dbh.users.find({"firstname":"jane"}, sort[("dateofbirth", pymongo.DESCENDING)])

# 検索した結果から指定した件数を取得する
dbh.users.find().sort(("score", pymongo.DESCENDING)).limit(10)
dbh.users.find().sort(("surname", pymongo.ASCENDING)).limit(20).skip(20)

# Snapshotモードを使う
for user in dbh.users.find(snapshot=True):
    print user.get("username"), user.get("score", 0)

# ドキュメントをupdateする
dbh.users.update({"firstname":"jane"}, {"$set":{"email":"janedoe74@example2.com", "score":1}}, safe=True)

# 条件に合致したすべてのドキュメントをupdateする
dbh.users.update({"score":0}, {"$set":{"flagged":True}}, multi=True, safe=True)

# ドキュメントを削除する
dbh.users.remove({"score":1}, safe=True)

# コレクションの中のすべてのドキュメントを削除する
dbh.users.remove(None, safe=True)