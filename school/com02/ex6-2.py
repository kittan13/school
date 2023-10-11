a = 0
counter = 0
while a <= 30 :
    counter = counter + 1
    if counter % 2 == 0:
        a = a + counter
    else:
        a = a - counter

    
print("1+2+...+nが10を超えるのは"+str(counter)+"をかけた時である。")