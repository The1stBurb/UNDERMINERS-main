#https://docs.google.com/document/d/1c2sKY1Q4PDsK8h_j1TRbw3K_OkEq5jbrHTj6mb4z3LY/edit?tab=t.0
from items.oreuh import brck,nts,no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt,hts,pick,charcor_pick,nevelium_pick,sword,charcor_sword,charium_sword,nevelium_sword,burb,craft
from base_funcs import *
from bobs import xny,bobs,boblst
from Loot.looter import gitStf

from time import sleep
from random import randint,choice

import saveus.piler as piler,sys,keyboard,mouse
import pygame
import logging

# Configure the logging system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',filename="logs.log")

# Create a logger
logger = logging.getLogger(__name__)
print("Your name is Bob! You live here now ig, so i hope yr happy!")
# input()
pygame.init()
X = 1000
Y = 1000
scrn = pygame.display.set_mode((X, Y))#,pygame.FULLSCREEN)
clk=pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
# font = pygame.font.Font('Middlecase-Regular.ttf', 20)
class chest52(brck):
    def __init__(self,nm,disp,sprd,num,pronc,mnLvl,roleth):
        super().__init__(nm,disp,sprd,num,pronc,mnLvl,col=(119,69,19))
        self.holds=[
            [itm(dirt,10),itm(void,0),itm(void,0),],
            [itm(void,0),itm(void,0),itm(void,0),],
            [itm(void,0),itm(void,0),itm(void,0),],
            ]
        r=roleth
        while len(r)>0:
            x,y=randint(0,2),randint(0,2)
            if self.holds[y][x].tp.nm=="void":
                ch=choice(r)
                self.holds[y][x]=itm(ch[0],ch[1])
                r.remove(ch)
    def prHold(self,p,m,ck):
        ms=xny(-1,-1)
        x1=x2=y1=y2=-1
        flis=flis2="chest"
        while True:
            scrn.fill((255,255,255))
            if x1!=-1 and y1!=-1:
                rect(x1*110,y1*110,110,100,col=(0,200,200))
            if x2!=-1 and y2!=-1:
                rect(x2*110,y2*110,110,100,col=(200,0,200))
            p.prInv1()
            for a,i in enumerate(self.holds):
                for b,j in enumerate(i):
                    if j.tp in nts:
                        if j.tp.nm=="void":
                            scrn.blit(colorize(vbrcck,j.tp.col),(b*110+550,a*110))    
                        else:
                            scrn.blit(colorize(brcck,j.tp.col),(b*110+550,a*110))
                    elif j.tp in hts:
                        if j.tp.tp=="pick":
                            scrn.blit(colorize(picck,j.tp.col),(b*110+560,a*110))
                        elif j.tp.tp=="sword":
                            scrn.blit(colorize(swrocc,j.tp.col),(b*110+560,a*110))
                    text(f"{j.no}x {j.tp.nm}",b*110+560,a*110+85)
            rect(900,900,100,100,col=(255,0,0))
            text("EXIT",900,900)
            rect(650,0,50,20,col=(200,200,200))
            text("MOVE",652,2)
            text(f"{ms.x},{ms.y},{int(ms.x/110)},{int(ms.y/110)}",0,900)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    ms.x,ms.y=pygame.mouse.get_pos()
            if ms.x>900 and ms.y>900:
                return
            elif ms.x<880 and ms.y<660 and ms.x>0 and ms.y>0:
                x,y=int(ms.x/110),int(ms.y/110)
                # print(x,y)
                # print(int(ms.x/110),int(ms.y/100))
                if x1==-1 or y1==-1:
                    x1,y1=x,y
                    if x1>=5 and y1>3:
                        x1=y1=-1
                    if x1<5:
                        flis="inv"
                # flis2="chest"
                # if x2<=5:
                #     flis2="inv"
                elif x1==x and y1==y:
                    x1=y1=-1
                    flis="chest"
                elif x2==-1 or y2==-1:
                    x2,y2=x,y
                    if x2>=5 and y2>3:
                        x2=y2=-1
                    if x2<5:
                        flis2="inv"
                elif x2==x and y2==y:
                    x2=y2=-1
                    flis2="chest"
            elif (ms.x>650 and ms.x<700 and ms.y<20 and x1!=-1 and x2!=-1 and y1!=-1 and y2!=-1) or (x2!=-1 and y2!=-1):
                if flis=="chest":
                    x1-=5
                if flis2=="chest":
                    x2-=5
                # print(x1,y1,flis,x2,y2,flis2)
                it1,it2=(self.holds if flis=="chest"else p.hold)[y1][x1],(self.holds if flis2=="chest"else p.hold)[y2][x2]
                if it1.tp.nm==it2.tp.nm:
                    it1.no+=it2.no
                    it2=itm(void,0)
                (self.holds if flis=="chest"else p.hold)[y1][x1],(self.holds if flis2=="chest"else p.hold)[y2][x2]=it2,it1
                x1=x2=y1=y2=-1
                flis=flis2="chest"
            pygame.display.flip()
            ms.x,ms.y=-1,-1
chest=chest52("chest","C",1,10,"chest",0,[])
nts.append(chest)
sz=50
class mos:
    def __init__(self,ck):
        self.ix=0
        self.iy=0
        if ck:
            self.init()
    def get(self):
        gp=mouse.get_position()
        return xny(gp[0]-self.ix,gp[1]-self.iy)
    def init(self):
        print("\033c",end="")
        # print("asdlkjandskgksa")
        print("\033[42m\033[31m#\033[0m  CLICK ON THE HASH with the LEFT button! If you do not the game will not WORK",1,1)
        while self.ix==0 and self.iy==0:
            sleep(0.1)
            prat(self.__str__()+" "*10,1,2)
            # right side-332,687
            # left side-322,687
            # top side-327,700
            # bottom side-327,700
            #md-327,687
            #wdth=7
            #height=14
            #so top left px is 324,681
            #btm right px is 330,694
            print()
            if mouse.is_pressed():
                got=self.get()
                self.ix=got.x
                self.iy=got.y
    def ip(self):
        return mouse.is_pressed()
    def __str__(self):
        g=self.get()
        return f"{round(g.x)},{round(g.y)}"
clickify=False
m=mos(clickify)
def roll():
    rolled=[]
    while len(rolled)<randint(3,9):
        ch=choice(gitStf())
        if randint(0,100)<=ch[1]:
            rolled.append([ch[0],randint(ch[2][0],ch[2][1])])
    roll2=[]
    for i in rolled:
        if str(i[0])[-1]=="0":
            if int(i[0]/10)<len(nts):
                roll2.append([nts[int(i[0]/10)],i[1]])
        else:
            if int(i[0]/10)<len(hts):
                roll2.append([hts[int(i[0]/10)],i[1]])
    return roll2
#this makes cool shapes
def get_dir(n):
    if n==0:#up
        return choice([3,1,2])
    elif n==1:#right
        return choice([2,0,3])
    elif n==2:#left
        return choice([1,0,3])
    elif n==3:#down
        return choice([0,1,2])
class tiles:
    def __init__(self):
        self.mw=10
        self.mh=10
        self.ben=[]
        self.bit=[[2 for j in range(self.mw)]for i in range(self.mh)]
        self.do_gen2()
    #get the neighbors of a tile
    def gNbr(self,x,y):
        tkn=[[-1,-1,-1],[-1,-2,-1],[-1,-1,-1],]
        for y1 in range(-1,1):
            for x1 in range(-1,1):
                if inr(x+x1,0,self.mw) and inr(x+y1,0,self.mh):
                    if self.bit[y+y1][x+x1]!=-1 :#and y1!=0 and x1!=0:
                        tkn[y1+1][x1+1]=self.bit[y+y1][x+x1]
                else:
                    tkn[y1+1][x1+1]=-2
        return tkn
    #is the map fully generated?
    def gtg(self):
        # gd=False
        for i in self.bit:
            if -1 in i:
                # gd=True
                return True
        return False
    #generates a single tile of the map
    def gen(self,cx=-1,cy=-1):
        #0-no_rock
        #1-placed rock
        #2-rock
        #3-dark rock
        #4-charium ore
        #5-nevlium ore
        #6-decante ore
        #7-charcor ore
        #just get the right x/y
        if cx==-1 or cy==-1:
            cx=randint(0,self.mw-1)
            cy=randint(0,self.mh-1)
        if cx>=self.mw:
            cx=self.mw-1
        if cy>=self.mh:
            cy=self.mh-1
        #this makes it so it dosen't try to place where its been
        if [cx,cy]in self.ben:
            return [-1,-1]
        else:
            self.ben.append([cx,cy])
        #gte its neighbors
        tkn=self.gNbr(cx,cy)
        cnt={-2:[],-1:[],0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for y,i in enumerate(tkn):
            for x,j in enumerate(i):
                cnt[j].append([x,y])
        if self.bit[cy][cx]!=-1:
            c=choice(cnt[-1])
            return cx+c[0]-1,cy+c[1]-1
        #get the most popular one, caus thats probally whats next!
        mp=[-1,0]
        for i in cnt:
            if i!=-1 and i!=-2:
                if len(cnt[i])>mp[1]+randint(-2,2):
                    mp=[i,len(cnt[i])]
        #But we gotta make sure its a good number, and rocks are more common!
        tl=mp[0]
        if tl==-1 or tl==8:
            tl=randint(0,len(nts)-1)
        if randint(0,3)==0:
            tl=3
        if randint(0,1)==0:
            tl=2
        #add it and return your face
        if self.bit[cy][cx]==-1:
            self.bit[cy][cx]=tl
        if len(cnt[-1])>0:
            c=choice(cnt[-1])
            return cx+c[0]-1,cy+c[1]-1
        else:
            return [-1,-1]
    #this just runs the generator
    def do_gen(self):
        #start genering at a random point
        x=randint(0,self.mw-1)
        y=randint(0,self.mh-1)
        q=[x,y]
        #generates it all
        while self.gtg():# and ir<500:
            ir+=1
            q=self.gen(q[0],q[1])
    #a better gen?
    def do_gen2(self):
        #how many spots
        clpr=(self.mw+self.mh)//2#+randint(-1,1)
        #run through them
        for i in range(clpr):
            #get a random spot/id for the stuff your adding
            tk=[randint(0,self.mw-1),randint(0,self.mh-1),randint(0,len(nts)-1),0]
            #we dont want placed rocks cause no people her right?
            if tk[2]==1 or tk[2]==8:
                continue
            #how many?
            tk[3]=nts[tk[2]].spr+randint(-1,1)
            #add a brick for each thingy
            grw=randint(0,3)
            for i in range(tk[3]):
                grw=get_dir(grw)
                #choose a dir^ and make the new x and y to place
                tk[0]=constrain(tk[0]+gd(grw)[0],0,self.mw-1)
                tk[1]=constrain(tk[1]+gd(grw)[1],0,self.mh-1)
                self.bit[tk[1]][tk[0]]=tk[2]
class MP:
    def __init__(self):
        self.mw=5
        self.mh=5
        self.mp=[[tiles() for j in range(self.mw)]for i in range(self.mh)]
        self.bit=[]
        self.tl=xny(0,0)
        self.data={}
        self.exp()
        self.bit[0][0]=0
        self.bit[0][1]=10
        self.datar()
    #add to the map on top
    def addUp(self):
        self.mh+=1
        self.tl.y+=1
        self.mp.append([tiles() for i in range(self.mw)])
    #add to the map on the right
    def addRgt(self):
        self.mw+=1
        for i in range(self.mh):
            self.mp[i].append(tiles())
        self.mw+=1
    #add to the map on bottom
    def addDwn(self):
        self.mh+=1
        self.mp.append([tiles() for i in range(self.mw)])
    #add to the map on the left
    def addLft(self):
        self.mw+=1
        self.tl.x+=1
        for i in range(self.mh):
            self.mp[i].insert(0,tiles())
    #Do all the adds
    def addOn(self,dirr):
        if dirr==0:
            self.addUp()
        elif dirr==1:
            self.addRgt()
        elif dirr==2:
            self.addDwn()
        elif dirr==3:
            self.addLft()
        if dirr in [0,1,2,3]:
            self.exp()
        # move(0,12)
        # print(dirr,self.tl)
    #not needed, would expand the map. idk if well finish and add
    def exp(self):
        #we want every top of the tiles across
        #then next, than next and so on till the bottom
        self.bit=[]
        for i in self.mp:
            #goes down
            for k in range(len(self.mp[0][0].bit)):
                #goes across each tile in the spot
                self.bit.append([])
                for j in i:
                    self.bit[-1].append(j.bit[k])
                    #goes across
        bit2=[]
        for i in self.bit:
            bit2.append([])
            for j in i:
                bit2[-1]+=j
        self.bit=bit2.copy()
    def datar(self):
        for a,i in enumerate(self.bit):
            for b,j in enumerate(i):
                if j==10:
                    self.data[f"{b},{a}"]=chest52("chest","C",1,10,"chest",0,roll())
    #runs the save code for JUST THE MAP, must be implemetned with the player and entity save codes!
    def save(self):
        return str(self.mp),str(self.mw),str(self.mh)
    def getTile(self):
        return self.mp[self.tl.y][self.tl.x]
dubloons=False
def colorize(image, new_color):
    tinted = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    tinted.fill(new_color)
    tinted.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted
class plr:
    def __init__(self):
        self.x=0
        self.y=0
        self.tx=0
        self.ty=0
        self.dir=1
        self.us=[pygame.transform.scale(pygame.image.load("images\\UP.png").convert_alpha(),(sz,sz)),pygame.transform.scale(pygame.image.load("images\\RIGHT.png").convert_alpha(),(sz,sz)),pygame.transform.scale(pygame.image.load("images\\DOWn.png").convert_alpha(),(sz,sz)),pygame.transform.scale(pygame.image.load("images\\LEFT.png").convert_alpha(),(sz,sz))]#"^",">","V","<"]
        self.hl=0
        self.mhp=10
        self.hp=self.mhp
        self.atk=1
        self.atkr=0
        self.ar=5
        self.dmgtk=False
        self.hold=[
            [itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],
            [itm(pick,1),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],]
    def dr(self,ox,oy):
        # rect(self.x*sz,self.y*sz,sz,sz,col=((255 if self.dir==0 or self.dir==3 else 0),(255 if self.dir==1 or self.dir==3 else 0),(255 if self.dir==2 or self.dir==3 else 0)))
        # rect(4.5*sz,4.5*sz,sz,sz,col=((255 if self.dir==0 or self.dir==3 else 0),(255 if self.dir==1 or self.dir==3 else 0),(255 if self.dir==2 or self.dir==3 else 0)))
        hl=100/self.mhp
        ys=800
        xs=10
        # quad(xs,ys,xs+10+self.hp*hl,ys,xs+self.hp*hl,ys+20,xs,ys+20,col=((0,0,0)if self.hp<hl else (0,255,0)))
        rect(0,ys,self.hp*hl,20,col=(0,255,0))
        text(f"Hp: {int(self.hp/self.mhp*100)}%",0,ys)
        if self.dmgtk:
            scrn.blit(colorize(self.us[self.dir],(255,0,0)),(4.5*sz,4.5*sz))
            self.dmgtk=False
        else:
            scrn.blit(self.us[self.dir],(4.5*sz,4.5*sz))
        rect(self.hl*110,900,110,100,col=(100,100,100))
        for a,i in enumerate(self.hold[5]):
            if i.tp in nts:
                scrn.blit(colorize(brcck,i.tp.col),(a*110,900))
            elif i.tp in hts:
                if i.tp.tp=="pick":
                    scrn.blit(colorize(picck,i.tp.col),(a*110+10,900))
                elif i.tp.tp=="sword":
                    scrn.blit(colorize(swrocc,i.tp.col),(a*110+10,900))
            scrn.blit(font.render(f"{i.no}x {i.tp.nm}", True, (0, 0, 0)),(a*110+10,975))
    def oub(self):
        global mp,pr
        isd=False
        if self.dir==0 and self.y<0:
            self.y=9
            mp.tl.y-=1
            isd=True
        elif self.dir==1 and self.x>9:
            self.x=0
            mp.tl.x+=1
            isd=True
        elif self.dir==2 and self.y>9:
            self.y=0
            mp.tl.y+=1
            isd=True
        elif self.dir==3 and self.x<0:
            self.x=9
            mp.tl.x-=1
            isd=True
        if isd:
            mp.addOn(self.dir)
            pr(0,0)
    def mover(self,d):
        global mp
        self.atkr+=0.1
        if d=="atk":
            # print("ou")
            if self.atkr>=self.ar:
                self.atkr=0
                # print("ouch")
                for i in bobs:
                    if (abs(i.x-self.x)<3 and abs(i.y-self.y)<3):
                        i.hp-=self.atk+self.hnd().tp.atk
                        i.dmgtk=True
                        # print("bonk")
            return
        elif d.isdigit() and inr(int(d)-1,0,5):
            self.hl=int(d)-1
            return
        elif d=="]":
            return
        elif d=="":
            return
        elif d=="i":
            self.prInv()
            return
        elif d=="o":
            # keyboard.send("backspace")
            mv=gd(self.dir)
            if self.y+mv[1]<0 or self.y+mv[1]>len(mp.bit)-1:
                return
            if self.x+mv[0]<0 or self.x+mv[0]>len(mp.bit[self.y+mv[1]])-1:
                return
            if mp.bit[self.y+mv[1]][self.x+mv[0]]==10:
                c=mp.data[f"{self.x+mv[0]},{self.y+mv[1]}"]
                c.prHold(self,m,clickify)
                sleep(0.5)
                print("\033c")
                pr(self.x,self.y)
            return
        elif d=="p":
            mv=gd(self.dir)
            if self.y+mv[1]<0 or self.y+mv[1]>len(mp.bit)-1:
                return
            if self.x+mv[0]<0 or self.x+mv[0]>len(mp.bit[self.y+mv[1]])-1:
                return
            if mp.bit[self.y+mv[1]][self.x+mv[0]]==0:
                if not self.hnd().tp.idd in [0,8] and self.hnd().tp.pcb:
                    mp.bit[self.y+mv[1]][self.x+mv[0]]=self.hnd().tp.idd
                    self.hold[5][self.hl].no-=1
                    self.fixInv()
            return
        elif d=="b":
            dr=gd(self.dir)
            nx,ny=self.x+dr[0],self.y+dr[1]
            if ny<0 or ny>len(mp.bit)-1:
                return
            if nx<0 or nx>len(mp.bit[ny])-1:
                return
            if self.hnd().tp.ms>=nts[mp.bit[ny][nx]].ml:
                if mp.bit[ny][nx]==10:
                    c=mp.data[f"{nx},{ny}"]
                    for i in c.holds:
                        for j in i:
                            self.addItm(j)
                self.addItm(nts[mp.bit[ny][nx]])
                mp.bit[ny][nx]=0
                # move(nx+1,ny+1)
                # print(no_rock)
        elif d in "zxcv":
            pd=self.dir
            self.dir={"z":0,"x":1,"c":2,"v":3}[d]
            if pd!=self.dir:
                return
        if d in["z","x","c","v","b"]:
            mv=gd(self.dir)
            drw=(self.x%10 and self.dir==1) or ((self.x-1)%10 and self.dir==3)or(self.y%10 and self.dir==2) or ((self.y-1)%10 and self.dir==0)
            self.y=1 if self.y+mv[1]<0 else(len(mp.bit)-2 if self.y+mv[1]>len(mp.bit)-1 else self.y)
            self.x=1 if self.x+mv[0]<0 else(len(mp.bit[self.y+mv[1]])-2 if self.x+mv[0]>len(mp.bit[self.y+mv[1]])-1 else self.x)
            if self.y+mv[1]>=0 and self.y+mv[1]<len(mp.bit) and self.x+mv[0]>=0 and self.x+mv[0]<len(mp.bit[self.y+mv[1]]):
                if mp.bit[self.y+mv[1]][self.x+mv[0]]==0:
                    self.y,self.x=self.y+mv[1],self.x+mv[0]
        self.dr(self.x-mv[0],self.y-mv[1])
    def prInv(self):
        ms=xny(-1,-1)
        x1=x2=y1=y2=-1
        while True:
            scrn.fill((255,255,255))
            if x1!=-1 and y1!=-1:
                rect(x1*110,y1*110,110,100,col=(0,200,200))
            if x2!=-1 and y2!=-1:
                rect(x2*110,y2*110,110,100,col=(200,0,200))
            for a,i in enumerate(self.hold):
                for b,j in enumerate(i):
                    if j.tp in nts:
                        if j.tp.nm=="void":
                            scrn.blit(colorize(vbrcck,j.tp.col),(b*110,a*110))    
                        else:
                            scrn.blit(colorize(brcck,j.tp.col),(b*110,a*110))
                    elif j.tp in hts:
                        if j.tp.tp=="pick":
                            scrn.blit(colorize(picck,j.tp.col),(b*110+10,a*110))
                        elif j.tp.tp=="sword":
                            scrn.blit(colorize(swrocc,j.tp.col),(b*110+10,a*110))
                    text(f"{j.no}x {j.tp.nm}",b*110+10,a*110+85)
            rect(900,900,100,100,col=(255,0,0))
            text("EXIT",900,900)
            rect(650,0,50,20,col=(200,200,200))
            text("MOVE",652,2)
            rect(650,60,55,20,col=(200,200,200))
            text("CRAFT",652,62)
            rect(650,30,60,20,col=(200,200,200))
            text("COLOUR",652,32)
            # text(f"{ms.x},{ms.y},{int(ms.x/110)},{int(ms.y/110)}",0,900)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    ms.x,ms.y=pygame.mouse.get_pos()
            if ms.x>900 and ms.y>900:
                return
            elif ms.x>650 and ms.x<700 and ms.y>30 and ms.y<50 and x1!=-1 and y1!=-1:
                self.colourify(x1,y1)
                x1=y1=-1
            elif ms.x>650 and ms.x<700 and ms.y>60 and ms.y<80 and x1!=-1 and y1!=-1:
                # self.craft(x1,y1)
                x1=y1=-1
            elif ms.x<650 and ms.y<750 and ms.x>0 and ms.y>0:
                x,y=int(ms.x/110),int(ms.y/110)
                print(x,y)
                # print(int(ms.x/110),int(ms.y/100))
                if x1==-1 or y1==-1:
                    x1,y1=x,y
                elif x1==x and y1==y:
                    x1=y1=-1
                elif x2==-1 or y2==-1:
                    x2,y2=x,y
                elif x2==x and y2==y:
                    x2=y2=-1
            elif (ms.x>650 and ms.x<700 and ms.y<20 and x1!=-1 and x2!=-1 and y1!=-1 and y2!=-1) or (x2!=-1 and y2!=-1):
                it1,it2=self.hold[y1][x1],self.hold[y2][x2]
                if it1.tp.nm==it2.tp.nm:
                    it1.no+=it2.no
                    it2=itm(void,0)
                self.hold[y1][x1],self.hold[y2][x2]=it2,it1
                x1=x2=y1=y2=-1
            pygame.display.flip()
            ms.x,ms.y=-1,-1
    def prInv1(self):
        for a,i in enumerate(self.hold):
                for b,j in enumerate(i):
                    if j.tp in nts:
                        if j.tp.nm=="void":
                            scrn.blit(colorize(vbrcck,j.tp.col),(b*110,a*110))    
                        else:
                            scrn.blit(colorize(brcck,j.tp.col),(b*110,a*110))
                    elif j.tp in hts:
                        if j.tp.tp=="pick":
                            scrn.blit(colorize(picck,j.tp.col),(b*110+10,a*110))
                        elif j.tp.tp=="sword":
                            scrn.blit(colorize(swrocc,j.tp.col),(b*110+10,a*110))
                    text(f"{j.no}x {j.tp.nm}",b*110+10,a*110+85)
    def addItm(self,item):
        if not isinstance(item,itm):
            item=itm(item,1)
        if item.tp.idd==0:
            return
        for i in range(5,-1,-1):
            for j in range(5):
                if self.hold[i][j].tp.nm==item.tp.nm:
                    self.hold[i][j].no+=item.no
                    return
        for i in range(5,-1,-1):
            for j in range(5):
                if self.hold[i][j].tp.nm=="void":
                    self.hold[i][j]=item
                    return
    def fixInv(self):
        for a,i in enumerate(self.hold):
            for b,j in enumerate(i):
                if j.no<=0:
                    self.hold[a][b]=itm(void,0)
    def hnd(self):
        return self.hold[5][self.hl]
    def colourify(self,ix,iy):
        print(ix,iy,"ooga")
        cc=self.hold[iy][ix].tp.col#repr()
        # if cc=="":
            # cc=repr("\033[48;2;0;0;0m")
        # cc=cc[:-2].split(";")
        b,g,r=int(cc[2]),int(cc[1]),int(cc[0])
        # r=g=b=0
        ms=xny(-1,-1)
        # x1=x2=y1=y2=-1
        while True:
            scrn.fill((255,255,255))
            rect(100,0,255,255,col=(r,g,b))
            rect(0,0,30,255,col=(r,0,0))
            text(str(r),2,257,col=(0,0,0))
            rect(40,0,30,255,col=(0,g,0))
            text(str(g),42,257,col=(0,0,0))
            rect(90,0,30,255,col=(0,0,b))
            text(str(b),92,257,col=(0,0,0))
            rect(0,r,30,10,col=(255,255,255))
            rect(40,g,30,10,col=(255,255,255))
            rect(90,b,30,10,col=(255,255,255))
            rect(900,900,100,100,col=(255,0,0))
            text("EXIT",900,900)
            text(f"{ms.x},{ms.y},{int(ms.x/110)},{int(ms.y/110)}",0,900)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
            if pygame.mouse.get_pressed()[0]:
                ms.x,ms.y=pygame.mouse.get_pos()
            if ms.x<30 and ms.y<255 and ms.x>0 and ms.y>0:
                r=ms.y
            elif ms.x>40 and ms.x<70 and ms.y<255 and ms.y>0:
                g=ms.y
            elif ms.x>90 and ms.x<120 and ms.y<255 and ms.y>0:
                b=ms.y
            elif ms.x>900 and ms.y>900:
                self.hold[iy][ix].tp.col=(r,g,b)
                return
            pygame.display.flip()
            ms.x,ms.y=-1,-1
        
p=plr()

mp=MP()
def resize(img,w,h):
    return pygame.transform.scale(img,(w,h))
def rot90(img,r=-1):
    if r==-1:
        r=randint(0,3)*90
    return pygame.transform.rotate(img,r)
def rect(x,y,w,h,col=(255,255,255)):
    # print(col)
    pygame.draw.rect(scrn, col, pygame.Rect(x, y, w, h))
def text(txt,x,y,col=(0,0,0)):
    scrn.blit(font.render(txt, True, col),(x,y))
def quad(x1,y1,x2,y2,x3,y3,x4,y4,col=(255,255,255)):
    pygame.draw.polygon(scrn, col, [(x1,y1),(x2,y2),(x3,y3),(x4,y4),])
brcck = pygame.transform.scale(pygame.image.load("images\\brick_base.png").convert_alpha(),(100,100))
vbrcck=brcck
vbrcck.set_alpha(0)
picck = pygame.transform.scale(pygame.image.load("images\\pick_base.png").convert_alpha(),(60,60))
swrocc=pygame.transform.scale(pygame.image.load("images\\sword_base.png").convert_alpha(),(60,60))
# bobck=pygame.transform.scale(pygame.image.load("images\\guy_down.png").convert_alpha(),(sz,sz))
bobcks=[
    [pygame.transform.scale(pygame.image.load("images\\Green_Gloop\\up.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Green_Gloop\\right.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Green_Gloop\\down.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Green_Gloop\\left.png").convert_alpha(),(sz,sz)),],

    [pygame.transform.scale(pygame.image.load("images\\Spagler\\up.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Spagler\\right.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Spagler\\down.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Spagler\\left.png").convert_alpha(),(sz,sz)),],

    [pygame.transform.scale(pygame.image.load("images\\Phuflee\\up.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Phuflee\\right.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Phuflee\\down.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Phuflee\\left.png").convert_alpha(),(sz,sz)),],

    [pygame.transform.scale(pygame.image.load("images\\Jeremy\\up.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Jeremy\\right.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Jeremy\\down.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\Jeremy\\left.png").convert_alpha(),(sz,sz)),],

    [colorize(pygame.transform.scale(pygame.image.load("images\\rock_base.png").convert_alpha(),(sz,sz)),rock.col),
     colorize(pygame.transform.scale(pygame.image.load("images\\Detrinium\\up.png").convert_alpha(),(sz,sz)),rock.col),
     pygame.transform.scale(pygame.image.load("images\\rock_base.png").convert_alpha(),(sz,sz)),
     pygame.transform.scale(pygame.image.load("images\\rock_base.png").convert_alpha(),(sz,sz)),],
]
rocck=pygame.transform.scale(pygame.image.load("images\\rock_base.png").convert_alpha(),(sz,sz))
ore=pygame.transform.scale(pygame.image.load("images\\ore_spots.png").convert_alpha(),(sz,sz))
cchest=pygame.transform.scale(pygame.image.load("images\\chest_base.png").convert_alpha(),(sz,sz))
#scaled_image = pygame.transform.scale(image, (new_width, new_height))
def pr(x,y):
    dx=(p.x+0.5-5)*sz
    dy=(p.y+0.5-5)*sz
    # move(1,1)
    szz=12
    x2=max(0,x-szz)
    y2=max(0,y-szz)
    for i in range(len(mp.bit)):#y2,min(y2+szz,len(mp.bit))):
        for j in range(len(mp.bit[i])):#x2,min(x2+szz,len(mp.bit[i]))):
            if abs(i-y)>12 or abs(j-x)>15:
                continue
            tp=mp.bit[i][j]
            aired=tp in[0,1,8] or (i>0 and mp.bit[i-1][j]in[0,1,8]) or (i<len(mp.bit)-1 and mp.bit[i+1][j]in[0,1,8]) or (j>0 and mp.bit[i][j-1]in[0,1,8]) or (j<len(mp.bit[i])-1 and mp.bit[i][j+1]in[0,1,8])
            if aired:
                if tp in [0,8]:
                    rect(j*sz-dx,i*sz-dy,sz,sz,nts[tp].col)
                elif tp in [4,5,6,7]:
                    # r=randint(0,3)*90
                    scrn.blit(rocck,(j*sz-dx,i*sz-dy))
                    scrn.blit(colorize(ore,nts[tp].col),(j*sz-dx,i*sz-dy))
                elif tp==10:
                    scrn.blit(colorize(cchest,nts[tp].col),(j*sz-dx,i*sz-dy))
                else:
                    scrn.blit(colorize(rocck,nts[tp].col),(j*sz-dx,i*sz-dy))
                    if tp==9:
                        scrn.blit(colorize(ore,nts[2].col),(j*sz-dx,i*sz-dy))
                    # rect(j*sz-dx,i*sz-dy,sz,sz,nts[tp].col)
            else:
                rect(j*sz-dx,i*sz-dy,sz,sz,(0,0,0))
    #DONT DELETE
    p.dr(p.x,p.y)
    ktp=[]
    for i in bobs:
        if i.dmgtk:
            i.dmgtk=False
            scrn.blit(colorize(bobcks[i.tp][i.dir],(255,0,0)),(i.x*sz-dx,i.y*sz-dy))
        else:
            scrn.blit(bobcks[i.tp][i.dir],(i.x*sz-dx,i.y*sz-dy))
        if not i.hp>0:
            bobs.remove(i)
        # i.disp((i.y,i.x))
def getSave():
    global mp
    b=""
    print("\033c")
    with open("saveus/save.pile","r")as sv:
        b=sv.readlines()[0].replace("\n","")
    evald=eval((b))#piler.dec
    mp.bit=evald[0]
    p.hold=[[eval(j) for j in i]for i in evald[1]]
    p.x,p.y=evald[2]
    mp.datar()
def writSave():
    global mp
    rs=[[repr(j)for j in i]for i in p.hold]
    # print(piler.enc([mp.bit,rs,(p.x,p.y)]))
    # return
    with open("saveus/save.pile","w")as sv:
        sv.write(str([mp.bit,rs,(p.x,p.y)]))#piler.enc
        sv.close()
        del sv
    print("SAVED")
if True:#intput("Get a new game, or use your old save? (new/old)")=="new":
    writSave()
else:
    getSave()
print("\033c")
pr(p.x,p.y)
# p.dr(p.x,p.y)
do=""
fps=calcFrm()
ts=time.time()
pk=["" for i in range(10)]
def texter():
    global pk
    pk=["" for i in range(10)]
    print("\033c")
    while True:
        pk.append(keyboard.read_key())
        sleep(0.1)
        prat(pk[-1],len(pk)-9,1)
        print("")
dev=False
up,right,down,left,save,w,a,s,d,place,brek,inv,openChest,space=pygame.K_UP,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_LEFT,pygame.K_u,pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_p,pygame.K_b,pygame.K_i,pygame.K_o,pygame.K_SPACE
k1,k2,k3,k4,k5=pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5
po=["",time.time()]
print(len(mp.bit),len(mp.bit[0]))
# mp.bit
mbt=0
tck=0
clickclack=[]
dmgtk=0
while True:
    if p.hp<=0:
        break
    scrn.fill((200,200,200))
    # mbt=1
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            # print(clickclack)
            quit()
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                kd=True
        elif i.type==pygame.MOUSEBUTTONDOWN:
            mbt=i.button
            # clickclack.append(pygame.mouse.get_pos())
        #DONT DELETE
        # if i.key==py.K_LSHIFT:# and br.ys<3:
        #     br.ys+=1
    keys=pygame.key.get_pressed()
    do=""
    if time.time()-po[1]>0.2:
        if keys[up]or keys[w]:
            do="z"
        elif keys[right]or keys[d]:
            do="x"
        elif keys[down]or keys[s]:
            do="c"
        elif keys[left]or keys[a]:
            do="v"
        elif keys[save]:
            do="]"
            writSave()
        elif keys[place]or mbt==3:
            mbt=0
            do="p"
        elif keys[brek]or mbt==1:
            mbt=0
            do="b"
        elif keys[inv]:
            do="i"
        elif keys[openChest]:
            do="o"
        elif keys[k1]:
            do="1"
        elif keys[k2]:
            do="2"
        elif keys[k3]:
            do="3"
        elif keys[k4]:
            do="4"
        elif keys[k5]:
            do="5"
        elif keys[space]:
            do="atk"
        if do==po[0] and po[0]!="" and time.time()-po[1]<0.5 and do in"zxcv":
            do="b"
        po=[do,time.time()]
    p.mover(do)
    clk.tick(50)
    tck+=1
    for i in bobs:
        i.run(mp.bit,[],p)
    pr(p.x,p.y)
    pygame.display.flip()
    if tck/50>5:#randint(10,15):
        tck=0
        print("HYE",tck)
        works=True
        while works:
            b=randint(0,len(mp.bit)-1)
            a=randint(0,len(mp.bit[b])-1)
            if mp.bit[b][a]==0:
                bobs.append(choice(boblst)(a,b))
                works=False
# font = pygame.font.Font('Middlecase-Regular.ttf', 20)
dth_mes=["You are ded",
        "You died",
        "You became a wee bit more dead than deadish",
        "You have found out whats afterlife",
        "Im so sorry for your loss","l",
        "womp womp",
        "You have met an untimely end! Better luck next time... or maybe just avoid the lava",
        "In the face of overwhelming odds, you fought valiantly. But even heroes must fall. Rest now, \"brave\" warrior.",
        "The shadows have claimed another soul. Your journey ends here, but the echoes of your deeds will linger in the realm. I'm not sure if thats a good thing tho",
        "Mate, I'm very much not even chuffed to bits at all with that performance. It was only a wee bit of impressive cause of how you died",
        "Oops! You tripped over your own feet and fell into oblivion. Don’t worry, it happens to the best of us—try again!",
        "Error 404: Player Not Found. Your consciousness has been uploaded to the cloud. Rebooting in 3... 2... 1...",
        "Congratulations! You've discovered a new way to lose. The game developers are both impressed and concerned.",
        "As the curtain falls on your final act, remember: in the game of life and pixels, everyone's battery eventually runs out.",
        "They say failure is the best teacher. By that logic, you're well on your way to becoming a genius! Try again, champ!",
        "Game over! You've been served a hot plate of defeat with a side of 'git gud'. Care for seconds?",
        "Et tu, Brute? Betrayed by your own reflexes. Caesar would understand.",
        "Forecast for your game: 100% chance of failure with scattered respawns throughout the afternoon.",
        "Have you tried turning yourself off and on again? No? Well, the game just did it for you.",
        "To die, or not to die - that was the question. Seems like you've found the answer.",
        "I'll be back... and so will you, after you hit that retry button!",
        ]
mes=choice(dth_mes)
dth_mes.remove(mes)
while True:
    scrn.fill((255,255,255))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            # print(clickclack)
            quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            if len(dth_mes)==0:
                quit()
            mes=choice(dth_mes)
            dth_mes.remove(mes)
    text(mes,0,Y/2)
    pygame.display.flip()