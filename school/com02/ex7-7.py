import random
GU = 0
CHOKI = 1
PA = 2
counter = 1

#毎回乱数が変わるようにします。
#random.seed()

#それぞれの手を決めます。
janken_com=random.randint(0,2)
janken_hito=int(input("あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2) :"))

#あいこか負けだと処理をくりかえす
while ((janken_com == janken_hito) or
        (janken_com==GU    and janken_hito==CHOKI) or 
         (janken_com==CHOKI and janken_hito==PA) or 
         (janken_com==PA    and janken_hito==GU)) :

        #あいこのとき
        if (janken_com == janken_hito):
            counter +=1 
            print("私の手は、" + str(janken_com)+ "でした。\n結果は、あいこです。", end="")
            janken_com=random.randint(0,2)
            janken_hito=int(input("\nもう一回チャンスを与えます。　\n あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2) :"))

        #負けのとき
        elif((janken_com==GU    and janken_hito==CHOKI) or 
            (janken_com==CHOKI and janken_hito==PA) or 
            (janken_com==PA    and janken_hito==GU)) :
            counter += 1
            print("私の手は、" + str(janken_com)+ "でした。\n結果は、私の勝ちです。", end="")
            janken_com=random.randint(0,2)
            janken_hito=int(input("\nもう一回チャンスを与えます。　\n あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2) :"))

        else:
            break



#勝ちのとき
if((janken_com==GU    and janken_hito==PA) or 
        (janken_com==CHOKI and janken_hito==GU) or 
        (janken_com==PA    and janken_hito==CHOKI)):
        print("私の手は、" + str(janken_com) + "でした。\n 結果は、あなたの勝ち",end="")


print("でした。")
print("あなたが私に勝つまでに"+ str(counter) + "回、挑戦しました。")