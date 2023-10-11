file = open("ex14-1.py","r",encoding ="utf-8")
while True:
    line = file.read()
    print(line)
    if not line:
        file.close()
        break