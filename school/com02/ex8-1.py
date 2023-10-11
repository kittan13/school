import tkinter

#ウィンドウの作成
root = tkinter.Tk()
root.title("長方形の描写")

#キャンバスの配置
canvas = tkinter.Canvas(root,width=640,height=480)
canvas.create_rectangle(250,250,350,350,fill ="grey78")
canvas.pack()

root.mainloop()