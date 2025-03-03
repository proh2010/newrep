import pygame as pg
class player():
    def __init__(self,x,y,image,speedx,speedy):
        self.x=x
        self.y=y
        self.image=image
        self.speedx=speedx
        self.speedy=speedy
    def update(self,l,r,u,d):
        if(self.speedx>0 and r==True):
            self.x=self.x+self.speedx
        elif(self.speedx<0 and l==True):
            self.x=self.x+self.speedx
        else:
            self.speedx=0
        if(self.speedy>0 and d==True):
            self.y=self.y+self.speedy
        elif(self.speedy<0 and u==True):
            self.y=self.y+self.speedy
        else:
            self.speedx=0
    def changeimage(self,image):
        self.image=image
    
class collider():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    
        self.left=pg.Rect((self.x+40,self.y+40,1,20*2+5))
        self.top=pg.Rect((self.x+43,self.y+37,20*2-3,1))
        self.right=pg.Rect((self.x+20*2+40,self.y+40,1,20*2+5))
        self.down=pg.Rect((self.x+43,self.y+20*2+47,20*2-3,1))
