import random
GU = 0
CHOKI = 1
PA = 2

#毎回乱数が変わるようにします。
#random.seed()

#それぞれの手を決めます。
janken_com=random.randint(0,2)
janken_hito=int(input("あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2) :"))

#結果を判断します。
print("私の手は、" + str(janken_com)+ "でした。\n 結果は、", end="")

#あいこの場合
if(janken_com == janken_hito) :
    print("あいこ",end="")
    

#コンピュータが勝つ場合
if((janken_com==GU    and janken_hito==CHOKI) or 
         (janken_com==CHOKI and janken_hito==PA) or 
         (janken_com==PA    and janken_hito==GU)) :
        print("私の勝ち",end="")

#人が勝つ場合
if((janken_com==GU    and janken_hito==PA) or 
        (janken_com==CHOKI and janken_hito==GU) or 
        (janken_com==PA    and janken_hito==CHOKI)):
        print("あなたの勝ち",end="")


print("でした。")