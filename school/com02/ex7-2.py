score = [70,60,70,55,40,90,100,85,72,31]

score_mini = 1000000000000000000000
for i in score:
    if(score_mini > i):
        score_mini = i
print("最小点数は、" + str(score_mini) + "点です。")