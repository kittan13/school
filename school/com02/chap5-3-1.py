import tkinter
import time
#ウィンドウ作成
root = tkinter.Tk()
root.title("棒グラフをソートして表示する")
#キャンバス配置
canvas = tkinter.Canvas(root,width=640,height=480)
canvas.create_rectangle(40,40,600,440,fill ="gray78")
canvas.pack()
#グラフ用変数
start_x = 60
start_y = 60
width_px = 5
height_px = 32
distance_px = 4
#リスト
list = [30,85,34,79,81,3,67,56,70,98]
# disp =""
#繰り返し処理
for k in range(len(list) - 1,0,-1):
    for j in range(0,k):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
    x = start_x
    y = start_y
    root.update()
    time.sleep(0.8)
    canvas.delete("graph")
    for i in list:
        canvas.create_rectangle(x,y,x+i*width_px,
        y+height_px,fill ="blue",outline = "blue",
        tag="graph")
        y = y+height_px+distance_px
        # disp = disp + str(i) + " "
    # print(disp)
    # disp = " "
root.mainloop()