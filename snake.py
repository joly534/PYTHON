from tkinter import *

fenetre = Tk()

canvas = Canvas(fenetre, width=600, height=600, background='green')
canvas.pack()



def case():
    x='0'
    y='0'
    w='20'
    h='20'
    bord="outline='black'"
    color="fill='yellow'"
    canvas.create_rectangle(x,y,w,h,bord,color)

def ligne():
    while x<580:
        canvas.create_rectangle(x,y,w,h,bord,color)
        x+=20
        w+=20

fenetre.mainloop()
