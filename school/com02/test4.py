score = [70,60,70,55,40,90,100,85,72,31,78,79,85]

score_max = 1
for i in score:
    if(score_max < i):
        score_max = i
print("最大点数は、" + str(score_max) + "点です。")