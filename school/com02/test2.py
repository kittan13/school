value = int(input("点数を入力してください:"))

if 0 <=value<=59:
    print("不合格")

elif 60<=value<=69:
    print("C")

elif 70<=value<=79:
    print("B")

elif 80<=value<=89:
    print("A")

elif 90<=value:
    print("S")

if 52<=value<=59:
    print("60点まで、あと"+str(60-value)+"点です。")