import random
GU = 0
CHOKI = 1
PA = 2

#毎回乱数が変わるようにします。
random.seed()

#それぞれの手を決めます。
janken_com=random.randint(0,2)
janken_hito=int(input("あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2) :"))


#結果を関数で表す
judge = (janken_hito - janken_com)%3 

#結果を判断します。
serihu = ("私の手は、" + str(janken_com)+ "でした。\n 結果は、")


#あいこの場合
if (judge == 0) :
    print(serihu + "あいこ")

#コンピュータが勝つ場合
elif (judge == 1) : 
    print(serihu + "あなたの負け")
#人が勝つ場合
elif (judge == 2) :
    print(serihu + "あなたの勝ち")

print("でした。")


