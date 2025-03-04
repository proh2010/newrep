import pygame as pg
def drf(f,col,b,xc,yc,l,w,ww):
    for i in range(len(f[l])):
        pg.draw.circle(w, col, ((f[l][i][0] * b + xc), (f[l][i][1] * b + yc)), 1)
def dr1(x1,c,x2,k,y1,y2,w,ww,fun):
    j=y1
    i = x1
    fun.append([])
    while i <= x2:
        j=y1
        while j<=y2:

            if c(i,j):
                fun[-1].append([i,j])




            j += k
        i+=k
def dr(x, c, b, n, k, xc, yc,col,hw,w,ww):
    xp = n
    i = n + k
    while i <= x:
        xn = i

        pg.draw.aaline(w, col, [xp * b + xc, ww - (c(xp) * b + yc)], [xn * b + xc, ww - (c(xn) * b + yc)])

        xp = xn
        i += k
