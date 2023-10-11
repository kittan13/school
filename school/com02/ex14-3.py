file = open("ex14-1.py","r",encoding ="utf-8")
door = open("ex14-3.txt","w",encoding="utf-8")
while True:
    line = file.read()
    key = door.write(str(line))
    if not line:
        file.close()
        door.close()
        break