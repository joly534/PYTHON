from tkinter import *
from math import pi, sin, cos

class Canon(object):
    def __init__(self, boss, x, y):
        self.boss = boss
        self.x1, self.y1 = x, y
        self.lbu = 50
        self.x2, self.y2 = x + self.lbu, y
        self.buse = boss.create_line(self.x1, self.y1, self.x2, self.y2, width = 10)
        r = 15
        boss.create_oval(x-r,y-r,x+r, y+r, fill='blue', width = 3)

    def orienter(self,angle):
        self.angle = float(angle)*2*pi/300
        self.x2 = self.x1 + self.lbu*cos(self.angle)
        self.y2 = self.y1 - self.lbu * sin(self.angle)
        self.boss.coords(self.buse,self.x1,self.y1, self.x2,self.y2)

if __name__ == '__main__':
    f = Tk()
    can = Canvas(f, width = 250, height = 250, bg = 'ivory')
    can.pack(padx = 10, pady = 10)
    c1 = Canon(can, 50, 200)

    s1 = Scale(f,label ='hausse', from_=90, to=0, command = c1.orienter)
    s1.pack(side=LEFT, pady = 5, padx = 20)
    s1.set(25)

    f.mainloop()

