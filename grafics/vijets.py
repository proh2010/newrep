import pygame as pg
class button():
    def __init__(self,w,wt,h,text,px,py,cl,f,s,cl2,cl3):
        self.w=w
        self.h=h
        self.text=text
        self.wt=wt
        self.px=px
        self.py=py
        self.cl=cl
        self.f=f
        self.s=s
        self.cl2=cl2
        self.cl3=cl3

    def pl(self,pos):
        kl=pg.font.Font(None,20)
        t=kl.render(self.text,True,(0,0,0))
        but=pg.Rect((self.px,self.py,self.wt,self.h))

        if(but.collidepoint(pos)):

            pg.draw.rect(self.w, self.cl2, (self.px, self.py,self.wt,self.h),border_radius=3)

        else:
            pg.draw.rect(self.w, self.cl, (self.px, self.py, self.wt,  self.h),border_radius=7)

        self.w.blit(t, (self.px + self.f, self.py + self.s))
    def to(self,pos,c,fl):
        f = pg.font.Font(None, 20)
        t = f.render(self.text, True, (0, 0, 0))
        but = pg.Rect((self.px, self.py, self.wt,self.h))
        if (but.collidepoint(pos)):
            pg.draw.rect(self.w, self.cl3, (self.px, self.py,self.wt,self.h),border_radius=3)
            if(fl):
                c()
        self.w.blit(t, (self.px + self.f, self.py + self.s))

