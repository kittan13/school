###############################
###        while,else文     ####
###############################

#whileの条件から抜けた際にelse文の処理の方に行くようにする。

count = 0

while count <5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

else:
    print("done")