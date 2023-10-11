file = open("ex14-2.txt","w",encoding="utf-8")
while True:
    key = file.write(str(input("何も入力せずにEnterを押すと終了します。\n")))
    if not key:
        file.close()
        break