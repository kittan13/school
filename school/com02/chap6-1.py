import tkinter

#ウィンドウ作成
root = tkinter.Tk()
root.title("ダンジョン＆バイソン")
root.minsize(840,454)
root.option_add("*font",["メイリオ",14])
#キャンバス作成
canvas = tkinter.Canvas(width=620,height=434)
canvas.place(x=10,y=10)
canvas.create_rectangle(0,0,620,434,fill="gray",tag="drawField")

#画像データを読み込み
images = [tkinter.PhotoImage(file="/home/kittan/com02/chap6-mapfield.png"),
          tkinter.PhotoImage(file="/home/kittan/com02/chap6-mapwall.png"),
          tkinter.PhotoImage(file="/home/kittan/com02/chap6-mapgoal.png"),
          tkinter.PhotoImage(file="/home/kittan/com02/chap6-mapkey.png"),
          tkinter.PhotoImage(file="/home/kittan/com02/chap6-mapman.png")]

root.mainloop()
