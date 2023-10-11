file = open("ex14-2.txt","w",encoding="utf-8")
for i in range(10):
    file.write(str(input()))
file.close