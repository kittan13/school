score = [100,50,30,45,24,60,68]
score_sum = 0
for i in range(len(score)):
    print(str(i) + "番目の点数は、" + str(score[i]) + "点です。")
    score_sum += score[i]
print("平均点は、" + str(round(score_sum/len(score),1)) + "点です。")