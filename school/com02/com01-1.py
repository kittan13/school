import tkinter

root = tkinter.TK()
root.title("計算機実習２")
root.minsize(640,480)

canvas = tkinter.Canvas(bg="black" , width=640 , height=480)
canvas.place(x=0 y=0)
img = tkinter.PhotoImage(file="chap3-back.png")
canvas.create_image(320,240,image=img)

root.mainloop()