list = [70,15,66,21,19,97,33,44,30,2]
disp =""
for k in range(len(list) - 1,0,-1):
    print(str(len(list) -k) + "度目")
    for j in range(0,k):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
        for i in list:
            disp = disp + str(i) + " "
        print(disp)
        disp = " "