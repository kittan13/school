############################################3
##         時間を扱う              #######
###########################################3

#import　datetimeで時間を扱うことができる。
import datetime

#datetime.datetime.nowで現在の時間を呼び出す。
now = datetime.datetime.now()
print(now)

today = datetime.datetime.today()
print(today)

"""
過去の時間などを扱いたい場合は datetime.timedelta("どれだけ前か")を用いる。
出力する際、変数は演算子を用いることができる。
"""

t = datetime.timedelta(weeks=1)
print(now-t)
t_2 = datetime.timedelta(days=1)
print(now - t_2)


#timeモジュールで他の時間も扱うことができる。
import time

print("####")
#time.sleepを使うことで、実行結果をその秒数間待ってもらうことができる
time.sleep(3)
print("#####")