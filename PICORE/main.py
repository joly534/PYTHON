from tkinter import *

fenetre = Tk()

canvas = Canvas(fenetre, width=1282, height=722)
canvas.pack()

#image de fond 
fond = PhotoImage(file="img/fond.gif")
canvas.create_image(0, 0,anchor='nw',  image=fond)


fenetre.mainloop()