birthmonth = int(input("あなたの生まれた月を入力してください："))
print(str(birthmonth)+"月は、",end="")

#四季に変換して判定する。春は3-5月、夏は6-8月、秋は9-11月、冬は12-2月
if int((birthmonth%12)/3) == 0:
    print("冬です。")
elif int((birthmonth%12)/3) == 1:
    print("春です。")
elif int((birthmonth%12)/3) == 2:
    print("夏です。")
elif int((birthmonth%12)/3) == 3:
    print("秋です。")
else:
    print("理解できません。")