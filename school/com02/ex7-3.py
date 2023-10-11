score = [80,60,70,65,80,90,100,15,72,31]
name = ["植村","藤井","中村","濱野","白石","箕浦","船戸","藤井","田中","鈴木"]
result=list(zip(score,name))
score = result
disp =""
for k in range(len(score)-1,0,-1):
    print(str(len(score) -k) + "度目")
for j in range(0,k):
    if score[j]>score[j+1]:
        temp = score[j]
        score[j] = score[j+1]
        score[j+1] = temp
    for i in score:
        disp = disp + str(i)+" "
    print(disp)
    disp=""
   