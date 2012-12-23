# coding: UTF-8
import time

# ローカルのタイムゾーンを考慮したstruct_timeシーケンスを返す
t = time.localtime()
print t

# 文字列を作る
print time.ctime()

# UTCにおけるエポック秒からの経過秒数を返す
print time.time()

# シーケンスをもとにエポック秒からの経過秒数を返す
print time.mktime(t)

# フォーマットで指定した文字列を返す
print time.strftime("%Y/%m/%d %H:%M:%S %a %Z")

# 文字列から日時のデータを得る
print time.strptime("2012/12/24 00:00:00 Mon JST", "%Y/%m/%d %H:%M:%S %a %Z")

# ローカルタイムゾーンのUTCからのオフセット
print time.timezone

# ローカルタイムゾーン名
print time.tzname

# 引数で与えた秒数だけ処理の実行を停止する
time.sleep(1)