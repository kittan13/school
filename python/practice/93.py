#######################################
######     ファイルの読み込み    ######
#########################################

s ="""\
AAA
BBB
CCC
DDD
"""


with open("text.txt","w") as f:
    #.readでファイルを読み込める。
    f.write(s)



#readlineを使うことで1行ずつ読み込むことができる。
with open("text.txt","r") as f:
    while True:
        line = f.readline()
        print(line ,end="")
        if not line:
            break


