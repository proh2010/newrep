import pygame as pg
import sprite as sp
import player as pl
pg.init()
w=pg.display.Info().current_w
h=pg.display.Info().current_h

screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
play = pl.player(300,850,sp.player,0,0)
playercol=pl.collider(play.x,play.y,20*2,20*2)
tery=32*8*2
terx=32*2
borderx=64
bordery=64
FPS = 20
colwp=[sp.box.get_rect(topleft=(128,1000-128))]
#print(colwp[1],playercol.down)
clock = pg.time.Clock()
plfr=0
plfl=0
running = True
playeranflag=0
d=1
fall=0
r=1
l=1
flag=0

def buildlevel(flag):
    screen.fill((0,0,0))
    for i in range(1,50):
        screen.blit(sp.terrain,(64*i,0),(borderx*2,bordery*3,64,64))
        if(flag==0):
            colwp.append(pg.Rect((64*i,0,64,64)))
    for i in range(1,50):
        screen.blit(sp.terrain,(0,64*i),(borderx*3,bordery*2,64,64))
        if(flag==0):
            colwp.append(pg.Rect((0,64*i,64,64)))
    for i in range(1,50):
        for j in range(1,50):
            screen.blit(sp.terrain,(64*i,64*j),(terx,tery,64,64))
    for i in range(1,50):
        screen.blit(sp.terrain,(64*i,1000),(borderx*2,bordery*1,64,64))
        if(flag==0):
            colwp.append(pg.Rect((64*i,1000,64,64)))
    screen.blit(sp.terrain,(64*16,1000-128),(borderx*2,bordery*5,64,64))
    if(flag==0):
        colwp.append(pg.Rect((64*16,1000-128,64,64)))
    screen.blit(sp.terrain,(64*15,1000-128),(borderx*1,bordery*5,64,64))
    if(flag==0):
        colwp.append(pg.Rect((64*15,1000-128,64,64)))
    screen.blit(sp.terrain,(64*17,1000-128),(borderx*3,bordery*5,64,64))
    if(flag==0):
        colwp.append(pg.Rect((64*17,1000-128,64,64)))
    flag=1
    screen.blit(sp.terrain,(64,0),(borderx*2,bordery*3,64,64))
    screen.blit(sp.terrain,(0,64),(borderx*3,bordery*2,64,64))
    screen.blit(sp.terrain,(0,0),(borderx*7,bordery,64,64))
    screen.blit(sp.terrain,(64,64),(terx,tery,64,64))
    screen.blit(sp.decoration,(64*4,64*4),(borderx*4,bordery*3,64*2,64*2))
    
    screen.blit(sp.decoration,(64*3,64*4),(borderx*1,bordery*1,64,64))
    screen.blit(sp.decoration,(64*3,64*5),(borderx*1,bordery*3,64,64))
    screen.blit(sp.decoration,(64*5.5,64*5),(borderx*1,bordery*3,64,64))
    screen.blit(sp.decoration,(64*5.5,64*4),(borderx*1,bordery*1,64,64))
    screen.blit(sp.box,(128,1000-128))
while running:
    
    buildlevel(flag)
    flag=1
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                plfr=1
            if event.key == pg.K_a:
                plfl=1
            if event.key == pg.K_SPACE:
                if(d==0):
                    play.speedy=-25
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                plfr=0
            if event.key == pg.K_a:
                plfl=0
    
    if (playercol.down.collidelist(colwp)!=-1):
        d=0
        
    else:
        d=1
        play.speedy+=1
        fall+=1
        
    if (plfr==1):
        play.speedx=10
    
    elif (plfl==1):
        play.speedx=-10
    else:
        play.speedx=0
        
    if(play.speedx!=0 and d==0):
        play.changeimage(sp.plgo)
        playeranflag+=1
        playeranflag=playeranflag%16
        
    else:
        playeranflag=0
        play.changeimage(sp.idle)
    if(d==1):
        play.changeimage(sp.jump)
    for i in range(fall):
        if (playercol.down.collidelist(colwp)==-1):
            play.y+=1
            playercol=pl.collider(play.x,play.y,58*2,58*2)
            
        
        else:
            fall=0
            play.speedy=0
            break
    if(play.speedx>0):
        for i in range(play.speedx):
            if (playercol.right.collidelist(colwp)==-1):
                play.x+=1
                playercol=pl.collider(play.x,play.y,58*2,58*2)
            
        
            else:
            
                break
    else:
        for i in range(-(play.speedx)):
            if (playercol.left.collidelist(colwp)==-1):
                play.x-=1
                playercol=pl.collider(play.x,play.y,58*2,58*2)
            
        
            else:
            
                break
    if(play.speedy<=0):
        for i in range(-(play.speedy)):
            if (playercol.top.collidelist(colwp)==-1):
                play.y-=1
                playercol=pl.collider(play.x,play.y,58*2,58*2)
            
        
            else:
                play.speedy=0
                break
    play.update(0,0,0,0)
    
    screen.blit(play.image,(play.x,play.y),((playeranflag//2)*78*2,0,78*2,58*2))
    playercol=pl.collider(play.x,play.y,58*2,58*2)
    #pg.draw.rect(screen,(0,0,0),playercol.down)
    #pg.draw.rect(screen,(0,0,0),playercol.top)
    #pg.draw.rect(screen,(0,0,0),playercol.right)
    #pg.draw.rect(screen,(0,0,0),playercol.left)
    
    pg.display.flip()
    
    clock.tick(FPS)

pg.quit()
