birthmonth = int(input("あなたの生まれた月を入力してください："))
print(str(birthmonth)+"月は、",end="")

#入力値を関数にする
season = int(birthmonth)

#四季に変換して判定する。春は3-5月、夏は6-8月、秋は9-11月、冬は12-2月
if 1<=season<=2 or season == 12:
    print("冬です。")
elif 3<=season<=5:
    print("春です。")
elif 6<=season<=8:
    print("夏です。")
elif 9<=season<=11:
    print("秋です。")
else:
    print("理解できません。")