import random
import tkinter


#ウィンドウ作成
root= tkinter.Tk()
root.title("じゃんけん大会！")
root.minsize(640,480)
root.option_add("*font",("メイリオ",14))

#画像読み込み
img1 = tkinter.PhotoImage(file='img4/janken_gu.png')
img2 = tkinter.PhotoImage(file='img4/janken_choki.png')
img3 = tkinter.PhotoImage(file='img4/janken_pa.png')
img4 = tkinter.PhotoImage(file='img4/akuma.png')

#キャンバス作成
canvas = tkinter.Canvas(root , width=640 , height=480)
canvas.place(x=0 , y=15)
canvas.create_image(320 , 220 ,image=img4 , tag="illust")

#ラベル配置
serihu_text = tkinter.Label(text= \
    "悪魔 「じゃんけんで私を倒すのだ！」")
serihu_text.place(x=160 , y=10)
janken_hito = tkinter.Label(text="あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2)",fg="red")
janken_hito.place(x=80 , y=380)

#入力ボックス配置
entry = tkinter.Entry(width=12)
entry.place(x=250 , y=420)


#ボタン配置
button = tkinter.Button(text="決定")
button.place(x=420 , y=415)


#定数決め
GU = 0
CHOKI = 1
PA = 2

#毎回乱数が変わるようにします。
random.seed()

#それぞれの手を決めます。
com=random.randint(0,2)
#janken=int(input("あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2) :"))

#結果を判断します。
#print("私の手は、" + str(com)+ "でした。\n 結果は、", end="")

#ボタンクリックイベント
def btn_click():
    janken = float(entry.get())

#あいこの場合
    if(com == janken) :

        canvas.delete("illust")
        canvas.create_image(320 , 220 , image=img1, tag="illust")
        serihu_text["text"] = "悪魔「なかなかやるな！」"
    

#コンピュータが勝つ場合
    if((com==GU    and janken==CHOKI) or 
         (com==CHOKI and janken==PA) or 
         (com==PA    and janken==GU)) :

        canvas.delete("illust")
        canvas.create_image(320 , 220 , image=img2, tag="illust")
        serihu_text["text"] = "勇者「ふっふっふ、私の勝ちだ！」"

#人が勝つ場合
    if((com==GU    and janken==PA) or 
        (com==CHOKI and janken==GU) or 
        (com==PA    and janken==CHOKI)):
        
        canvas.delete("illust")
        canvas.create_image(320 , 220 , image=img3, tag="illust")
        serihu_text["text"] = "悪魔「私が負けるとは！？」"


#button["state"] = "disabled"
#entry["state"] = "disabled"

#ボタンをクリックイベントと関数の関連付け
button["command"] = btn_click

root.mainloop()