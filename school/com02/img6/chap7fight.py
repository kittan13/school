import tkinter
from tkinter.constants import X

class FightManager:
    #コンストラクタ
    def __init__(self):
        self.dialog = tkinter.Frame(width=820, height=434)
        self.dialog.place(x=10,y=10)
        canvas = tkinter.Canvas(self.dialog,width=820,
height=434)
        canvas.place(x=0,y=0)
        canvas.create_rectangle(0,0,620,434,fill="black")
        #ボタン作成
        winbutton = tkinter.Button(self.dialog,text="勝った")
        winbutton.place(x=180,y=340)
        winbutton["command"] = self.fight_win
        runbutton = tkinter.Button(self.dialog,text="逃げた")
        runbutton.place(x=250,y=340)
        runbutton["command"] = self.fight_run
        losebutton = tkinter.Button(self.dialog,text="負けた")
        losebutton.place(x=320,y=340)
        losebutton["command"] = self.fight_lose
        #非表示
        self.dialog.place_forget()
    #戦闘開始
    def fight_start(self,map_date,x,y):
        self.dialog.place(x=10,y=10)
        self.map_date = map_date
        self.brave_x = x
        self.brave_y = y 
    #勝利
    def fight_win(self):
        self.map_date[self.brave_y][self.brave_x] = 0
        self.dialog.place_forget()
    #敗北
    def fight_lose(self):
        canvas = tkinter.Canvas(self.dialog,width=820,
    height=434)
        canvas.place(x=0,y=0)
        canvas.create_rectangle(0,0,620,434,fill="red")
        canvas.create_text(300,200,
            fill="white",font=("MS ゴシック",15),
            text="""勇者は負けてしまった。
    最初からやり直してくれたまえ。""")
    #逃げた
    def fight_run(self):
        self.map_date[self.brave_y][self.brave_x] = 5
        self.dialog.place_forget()