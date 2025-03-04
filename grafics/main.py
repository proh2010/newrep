import pygame as pg
from pygame import*
import math as m
import vijets as vj
import graf as gr
hw=1100
ww=800
def f2(x):
    return -1*x+0.5
def f1(x):
    return (1+1/3)*x-11/6

def co():
    global flt
    flt=not(flt)



def c(x,y):
    if(m.cos(m.cos(x**2)+y**2)>m.sin(m.sin(y**2)+x**2)-0.1 and m.cos(m.cos(x**2)+y**2)<m.sin(m.sin(y**2)+x**2)+0.1):
        return 1
    else:
        return 0



def kj():
    global fl
    if(fl==1):
        fl=0
    else:
        fl=1

pg.init()
ico=pg.image.load("icon.png")

w = pg.display.set_mode((hw, ww),pg.RESIZABLE)
pg.display.set_caption("Grafics")
pg.display.set_icon(ico)
run = True
xc = hw/2
yc = ww/2
b = 5
global k
k=0.1
global fan
#global fl
fl=0

fun=[]
flagb=0
but=vj.button(w,80,30,"Реж.сетки",20, 30,(200,200,200),7,9,(100,100,100),(50,50,50))
#gr.dr1(-25, c, 25, 0.02,-25,25,w,ww,fun)
but2=vj.button(w,60,20,"См.тему",20, 80,(200,200,200),4,3,(100,100,100),(50,50,50))
flt=0
save=open("save.txt","r")
flt=int(save.read(1))
save.close()
def func(x):
    return m.sin(x)*m.cos(x**2)
while run:
    ww=w.get_rect().height
    hw=w.get_rect().width
    xc = hw / 2
    yc = ww / 2
    #xc-=2
    #b += 0.05

    fon = pg.font.Font(None, int(1*b))
    k+=0.3

    if(flt):
        w.fill((0, 0, 0))
        text = fon.render("Пи", True, (255,255,255))

    else:
        w.fill((255, 255, 255))
        text = fon.render("Пи", True, (0,0,0))
    w.blit(text, (3.1415 * b + 0.2 * b+xc, ww - (yc - 1.1 * b)))


    if (fl == 1):
        if(flt==1):
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (255, 255, 255), [0, ww - (1 * i * b + yc)],[hw, ww - (1 * i * b + yc)])
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (255, 255, 255), [1 * i * b + xc, 0],[1 * i * b + xc, ww])
            pg.draw.aaline(w, (150, 150, 150), [3.1415 * b + xc, 0], [3.1415 * b + xc, ww])
        else:
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (0, 0, 0), [0, ww - (1 * i * b + yc)],[hw, ww - (1 * i * b + yc)])
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (0, 0, 0), [1 * i * b + xc, 0],[1 * i * b + xc, ww])
            pg.draw.aaline(w, (100, 100, 100), [3.1415 * b + xc, 0], [3.1415 * b + xc, ww])
    else:
        if(flt==1):
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (255, 255, 255), [xc - 2 * b, ww - (1 * i * b + yc)],[xc + 2 * b, ww - (1 * i * b + yc)])
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (255, 255, 255), [1 * i * b + xc, ww - (yc - 2 * b)],[1 * i * b + xc, ww - (yc + 2 * b)])
            pg.draw.aaline(w, (150, 150, 150), [3.1415 * b + xc, ww - (yc - 1 * b)],[3.1415 * b + xc, ww - (yc + 1 * b)])
        else:
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (0, 0, 0), [xc - 2 * b, ww - (1 * i * b + yc)],[xc + 2 * b, ww - (1 * i * b + yc)])
            for i in range(-5, 6, 1):
                pg.draw.aaline(w, (0, 0, 0), [1 * i * b + xc, ww - (yc - 2 * b)],[1 * i * b + xc, ww - (yc + 2 * b)])
            pg.draw.aaline(w, (100, 100, 100), [3.1415 * b + xc, ww - (yc - 1 * b)], [3.1415 * b + xc, ww - (yc + 1 * b)])

    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                but.to(pg.mouse.get_pos(),kj,1)
                but2.to(pg.mouse.get_pos(), co, 1)
                flagb = 1
            if i.button == 4:
                if b < 1000:
                    b *= 1.1
            if i.button == 5:
                if b > 0:
                    b /= 1.1
        if i.type == pg.MOUSEBUTTONUP:


            flagb = 0

    gr.dr(100, f1, b, -100, 0.05, xc, yc,(100,0,255),hw,w,ww)
    gr.dr(100, f2, b, -100, 0.05, xc, yc,(255,0,0),hw,w,ww)
    #gr.drf(fun,(0, 255, 0),b,xc,yc,0,w,ww)
    if(flt):
        pg.draw.aaline(w, (255, 255, 255), [0, ww - yc], [hw, ww - yc])
        pg.draw.aaline(w, (255, 255, 255), [xc, 0], [xc, hw])
    else:
        pg.draw.aaline(w, (0, 0, 0), [0, ww - yc], [hw, ww - yc])
        pg.draw.aaline(w, (0, 0, 0), [xc, 0], [xc, hw])
    but.pl(pg.mouse.get_pos())
    but2.pl(pg.mouse.get_pos())
    if (flagb == 1):
        but.to(pg.mouse.get_pos(), kj, 0)
        but2.to(pg.mouse.get_pos(), kj, 0)

    pg.display.update()
    time.delay(10)