import random

counter = 1
com = random.randint(1,1000)

print("数当てゲームです。頑張りましょ～")

hito = int(input("1～1000のなかで好きな数字を入力してください:"))

while ((com > hito) or
      (com < hito)):

    if (com > hito):
        counter +=1
        print("あなたの入力した数は、コンピュータより小さいです。")
        hito = int(input("もう一度挑戦です！\n1～1000のなかで好きな数字を入力してください:"))

    elif(com < hito):
        counter +=1
        print("あなたの入力した数は、コンピュータより大きいです。")
        hito = int(input("もう一度挑戦です！\n1～1000のなかで好きな数字を入力してください:"))

    else:
        break

if (com == hito):
    print("おめでとう！正解だよ！")

print("あなたがコンピュータと同じ数を当てるまでに"+ str(counter) + "回、挑戦しました。")