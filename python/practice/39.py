
#breakはループを終わらせ、countinueは次の処理を飛ばしてループにもどる。

count = 0


while True:
    #count += 1
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1


counter = 0

while counter < 5:
    print(counter)
    if counter == 2:
        counter += 1
        continue

    if counter == 3:
        break

    counter += 1
    print(counter)
