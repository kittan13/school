import tkinter
import math
#ウィンドウ作成
root = tkinter.Tk()
root.title("王様をいっぱい表示")
root.minsize(1280,800)
#キャンバス配置
canvas = tkinter.Canvas(root,width=1280,height=800)
canvas.pack()
img = tkinter.PhotoImage(file = "img4/chap4-1-1.png")
#繰り返し表示
math.radians=180
for i in range(6):
    canvas.create_image(640+math.radians*math.cos(45*i),305+math.radians*math.sin(45*i), image = img)
root.mainloop()
