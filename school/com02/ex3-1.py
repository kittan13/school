import tkinter

# ウィンドウ作成
root = tkinter.Tk()
root.title("先生にしつもん")
root.minsize(640,480) 
root.option_add("*font",["MS Pゴシック,22"])

#画像表示
canvas=tkinter.Canvas(bg="green",width=640,height=480)
canvas.place(x=0,y=0)
img=tkinter.PhotoImage(file="chap3-back.png")
canvas.create_image(320,240,image=img)

#テキスト表示
question=tkinter.Label(text="計算機実習２",bg="light blue")
question.place(x=100,y=40)

#テキストボックスを表示
entry=tkinter.Entry(width=12,bd=4)
entry.place(x=50,y=133)

#質問ボタン表示
askbutton=tkinter.Button(text="聞く")
askbutton.place(x=260,y=125)

#答え表示
answer=tkinter.Label(text="・・・・・・",bg="white")
answer.place(x=115,y=235)

#イベント設定
def ask_click():
    print("ボタンがクリックされました！")

askbutton["command"]=ask_click

# メインループ
root.mainloop()