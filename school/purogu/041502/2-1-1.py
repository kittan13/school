import datetime

target_date = int(input("日付を入力してください:"))

if 0<=target_date<=31:
    date=target_date%7

else:
    print("日付を入力してください。")

if date is 0:
    print("月曜日です。")

elif date is 1:
    print("火曜日です。")

elif date is 2:
    print("水曜日です。")

elif date is 3:
    print("木曜日です。")

elif date is 4:
    print("金曜日です。")

elif date is 5:
    print("土曜日です。")

elif date is 6:
    print("日曜日です。")
