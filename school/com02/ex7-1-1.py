score = [100,50,30,45,24,60,68,10,15,20,25,30,35,40,45,50,55,60,65,70]
score_sum = 0
for i in range(len(score)):
    print(str(i) + "番目の点数は、" + str(score[i]) + "点です。")
    score_sum += score[i]
print("平均点は、" + str(score_sum/len(score)) + "点です。")