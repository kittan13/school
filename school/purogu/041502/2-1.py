import datetime

a = int(input("年を入力してください:"))
b = int(input("月を入力してください:"))
c = int(input("日を入力してください:"))

t = datetime.date(a,b,c)

i=t.weekday()

if i is 0:
    print("月曜日です。")

elif i is 1:
    print("火曜日です。")

elif i is 2:
    print("水曜日です。")

elif i is 3:
    print("木曜日です。")

elif i is 4:
    print("金曜日です。")

elif i is 5:
    print("土曜日です。")

elif i is 6:
    print("日曜日です。")

