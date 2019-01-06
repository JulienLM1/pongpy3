#!/usr/bin/python
# -*- coding: UTF-8 -*-


from Tkinter import *
from random import randrange
J1=0
J2=0

tk=Tk()
tk.title("J1 : "+str(J1)+" Pong J2 : "+str(J2))


X=800
Y=600
VITESSE=5
COLOR="white"
BGCOLOR="black"

PLAY = True

class Pong :
    def __init__(self):
        self.tx=10
        self.ty=10
        self.r1=Raquette(30,Y/2-self.ty/2,"<z>","<s>")
        self.r2=Raquette(X-30,Y/2-self.ty/2,"<Up>","<Down>")
        self.dummy=randrange(0, 100)

        self.x=X/2-self.tx/2
        self.y=Y/2-self.ty/2
        self.dx=0
        if self.dummy < 50 :
            self.dx=-1
        else :
            self.dx=1

        self.dy=float(randrange(-100,100))/100

        self.balle=terrain.create_rectangle(self.x, self.y, self.x+self.tx, self.y+self.ty, fill=COLOR)
        self.deplacer()
        tk.bind_all("<Return>",self.pause)

    def pause(self, event):
        global PLAY
        if PLAY :
            PLAY = True
        else :
            PLAY = True

    def raffraichir(self):
        terrain.coords(self.balle, self.x, self.y, self.x+self.tx, self.y+self.ty)

    def deplacer(self):
        global J1, J2, PLAY
        if PLAY :
            self.x+=self.dx*VITESSE
            self.y+=self.dy*VITESSE

            if self.y <= 0 or self.y >= Y-self.ty :
                self.dy=-self.dy
            if self.r1.y<=self.y+self.ty and self.r1.y+self.r1.ty>=self.y :
                if self.x <= self.r1.x+self.r1.tx and not self.x+self.tx<=self.r1.x:
                    self.dx=-self.dx
                    self.dy=float(randrange(-100,100))/100

            if self.y <= 0 or self.y >= Y-self.ty :
                self.dy=-self.dy
            if self.r2.y<=self.y+self.ty and self.r2.y+self.r2.ty>=self.y :
                if self.x+self.tx <= self.r2.x and not self.x <= self.r2.x+self.r2.tx :
                    self.dy=float(randrange(-100,100))/100

            if self.x+self.tx<0 :
                self.x=X/2-self.tx/2
                self.y=Y/2-self.ty/2
                J2+=1
                self.dx=-self.dx
                self.dy=float(randrange(-100,100))/100
                self.r1.placer(30, Y/2-self.ty/2)
                self.r2.placer(X-30, Y/2-self.ty/2)
                PLAY=False


            if self.x+self.tx>X :
                self.x=X/2-self.tx/2
                self.y=Y/2-self.ty/2
                J1+=1
                self.dx=-self.dx
                self.dy=float(randrange(-100,100))/100
                self.r1.placer(30, Y/2-self.ty/2)
                self.r2.placer(X-30, Y/2-self.ty/2)
                PLAY=False



            tk.title("J1 : "+str(J1)+" Pong J2 : "+str(J2))
            self.raffraichir()

        tk.after(30,self.deplacer)


class Raquette :
    def __init__(self,x,y,haut,bas):
        self.x=x
        self.y=y
        self.tx=10
        self.ty=50
        self.vitesse=10
        self.haut=haut
        self.bas=bas
        self.ra=terrain.create_rectangle(self.x, self.y, self.x+self.tx, self.y+self.ty, fill=COLOR)
        tk.bind_all(self.haut,self.monter)
        tk.bind_all(self.bas,self.descendre)

    def monter(self,event):
        self.deplacer(-self.vitesse)
    def descendre(self,event):
        self.deplacer(self.vitesse)



    def deplacer (self,dy):
        if PLAY :
            self.y+=dy
            if self.y < 0 :
                self.y=0
            if self.y > Y-self.ty:
                self.y=Y-self.ty
            self.raffraichir()
    def placer(self,x,y):
        self.x=x
        self.y=y
        terrain.coords(self.ra, self.x, self.y, self.x+self.tx, self.y+self.ty)


    def raffraichir(self):
        terrain.coords(self.ra, self.x, self.y, self.x+self.tx, self.y+self.ty)



if __name__ == '__main__':
    tk.resizable(width=False, height=False)
    terrain=Canvas(tk, bg=BGCOLOR,height=Y, width=X)
    terrain.pack()
    ligne=terrain.create_rectangle(X/2-5,1,X/2+5,Y+1,fill=COLOR)
    jeu=Pong()

    tk.mainloop()
