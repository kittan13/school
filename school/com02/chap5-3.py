list = [70,15,66,21,19,97,33,44,30,2]
disp =""
for j in range(len(list) - 1):
    if list[j] > list[j + 1]:
        temp = list[j]
        list[j] = list[j + 1]
        list[j + 1] = temp
    for i in list:
        disp = disp + str(i) + " "
    print(disp)
    disp = " "