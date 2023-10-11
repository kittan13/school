counter = 0
hito = int(input("足したい数を入力してね:"))

sum = counter + hito

while (sum != 0):
    if sum !=0:
        print("計算結果は、" + str(sum)+ "だよ。")
        hito = int(input("足したい数を入力してね:"))
        sum += hito
        


    elif (sum ==0):
        break



