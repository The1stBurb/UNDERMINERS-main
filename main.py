#https://docs.google.com/document/d/1c2sKY1Q4PDsK8h_j1TRbw3K_OkEq5jbrHTj6mb4z3LY/edit?tab=t.0
from items.oreuh import nts,no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt,chest,chest52,hts,pick,charcor_pick,nevelium_pick,sword,charcor_sword,charium_sword,nevelium_sword,burb,craft
from base_funcs import *
from bobs import xny,bobs
from Loot.looter import gitStf

from time import sleep
from random import randint,choice

import saveus.piler as piler,sys,keyboard,mouse
import pygame
pygame.init()
X = 1000
Y = 999
scrn = pygame.display.set_mode((X, Y))
clk=pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

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
clickify=False#intput("Do you want to use your mouse? This DOESN'T ALWAYS work. Proceed with caution. (y/n)")=="y"
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
        self.mw=2
        self.mh=2
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
        move(0,12)
        print(dirr,self.tl)
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
class plr:
    def __init__(self):
        self.x=0
        self.y=0
        self.tx=0
        self.ty=0
        self.dir=1
        self.us=["^",">","V","<"]
        self.hl=0
        self.hold=[
            [itm(rock,5),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],[itm(void,0),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],
            [itm(pick,1),itm(void,0),itm(void,0),itm(void,0),itm(void,0),],]
    def dr(self,ox,oy):
        rect(self.x*10,self.y*10,10,10,col=((255 if self.dir==0 or self.dir==3 else 0),(255 if self.dir==1 or self.dir==3 else 0),(255 if self.dir==2 or self.dir==3 else 0)))
    def move(self,d):
        global mp
        if d=="b":
            dr=gd(self.dir)
            nx,ny=self.x+dr[0],self.y+dr[1]
            self.addItm()
            mp.getTile().bit[ny][nx]=0
            move(nx+1,ny+1)
            print(no_rock)
        elif d=="z":
            self.dir=0
        elif d=="x":
            self.dir=1
        elif d=="c":
            self.dir=2
        elif d=="v":
            self.dir=3
        ox,oy=self.x,self.y
        dx=self.x+gd(self.dir)[0]
        dy=self.y+gd(self.dir)[1]
        tk=0
        if dx>=0 and dx<=9 and dy>=0 and dy<=9:
            tk=mp.getTile().bit[dy][dx]
        if tk==0:
            self.x,self.y=dx,dy
        self.dr(ox,oy)
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
        if d.isdigit() and inr(int(d)-1,0,5):
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
                move(nx+1,ny+1)
                print(no_rock)
        elif d in "zxcv":
            self.dir={"z":0,"x":1,"c":2,"v":3}[d]
        mv=gd(self.dir)
        drw=(self.x%10 and self.dir==1) or ((self.x-1)%10 and self.dir==3)or(self.y%10 and self.dir==2) or ((self.y-1)%10 and self.dir==0)
        self.y=0 if self.y+mv[1]<0 else(len(mp.bit)-2 if self.y+mv[1]>=len(mp.bit)-1 else self.y)
        self.x=0 if self.x+mv[0]<0 else(len(mp.bit[self.y+mv[1]])-2 if self.x+mv[0]>=len(mp.bit[self.y+mv[1]])-1 else self.x)
        if self.y+mv[1]>=0 and self.y+mv[1]<len(mp.bit) and self.x+mv[0]>=0 and self.x+mv[0]<len(mp.bit[self.y+mv[1]]):
            if mp.bit[self.y+mv[1]][self.x+mv[0]]==0:
                self.y,self.x=self.y+mv[1],self.x+mv[0]
        self.dr(self.x-mv[0],self.y-mv[1])
        if drw:
            pr(self.x,self.y)
    def prInv(self):
        keyboard.send("backspace")
        while True:
            print("\033c")
            for b in range(5):
                prat(b+1,b*16+3,1)
            print("|")
            for a,i in enumerate(self.hold):
                prat(a+1,1,a+(3 if a==5 else 2))
                for b,j in enumerate(i):
                    prat("|"+str(j),(b)*16+3,(a)+(3 if a==5 else 2))
                print("|")
            print("\nRow 6 is the bar you can access anytime! |EXIT|")
            dor=intput("Would you like to move an item, custom color an item, craft or exit? (move,craft,exit,colour)")
            if dor=="move":
                x1,y1=gtInt("What is the X coordinate of the item?",1,5),gtInt("Whats the Y?",1,6)
                x2,y2=gtInt("What is the X coordinate of where you to move it?",1,5),gtInt("What is the Y?",1,6)
                # print(x1,y1,x2,y2)
                it1=self.hold[y1-1][x1-1]
                it2=self.hold[y2-1][x2-1]
                if it1.tp.nm==it2.tp.nm:
                    it1.no+=it2.no
                    it2=itm(void,0)
                self.hold[y1-1][x1-1],self.hold[y2-1][x2-1]=it2,it1
            elif dor=="exit":
                print("Exiting...")
                sleep(0.5)
                print("\033c")
                return
            elif dor=="craft":
                craft(self)
            elif dor=="colour":
                x1,y1=gtInt("What is the X coordinate of the item?",1,5),gtInt("Whats the Y?",1,6)
                self.colourify(x1,y1)
    def prInv1(self):
        for b in range(5):
            prat(b+1,b*16+3,1)
        for a,i in enumerate(self.hold):
            prat(a+1,1,a+(3 if a==5 else 2))
            for b,j in enumerate(i):
                prat("|"+str(j),(b)*16+3,(a)+(3 if a==5 else 2))
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
        cc=repr(self.hold[iy][ix].tp.col)
        if cc=="":
            cc=repr("\033[48;2;0;0;0m")
        cc=cc[:-2].split(";")
        g,b,r=int(cc[-1]),int(cc[-2]),int(cc[-3])
        print("\033c",end="")
        px,py=0,0
        ppx,ppy=px,py
        while not True:
                sleep(0.5)
                do=keyboard.read_key()
                if do=="up"and py>0:
                    py-=1
                elif do=="right"and px<15:
                    px+=1
                elif do=="down"and py<15:
                    py+=1
                elif do=="left"and px>0:
                    px-=1
                elif do=="enter":
                    break
                if ppx!=px and ppy!=py:
                    prat(" ",ppx+1,ppy+1)
                    print("")
                    prat("#",px+1,py+1)
                    print("")
                    prat(f"r:{(8-px+8-py)/2}, b:{(px+8-py)/2}, g:{(8-px+py)/2}",1,18)
                    print("")
                    ppx,ppy=px,py
        while True:
            r=gtInt("What do you want the red to be?",0,255)
            g=gtInt("What do you want the green to be?",0,255)
            b=gtInt("What do you want the blue to be?",0,255)
            good=intput(f"\033[48;2;{r};{g};{b}mIs this the right color? (y/n)\033[0m")
            if good=="y":
                break
        self.hold[iy][ix].tp.col=f"\033c[48;2;{r};{g};{b}"
        print(repr(self.hold[iy][ix].tp.col))
p=plr()

mp=MP()
def rect(x,y,w,h,col=(255,255,255)):
    # print(col)
    pygame.draw.rect(scrn, col, pygame.Rect(x, y, w, h))
def pr(x,y):
    dx=0#p.x-50
    dy=0#p.y-50
    # move(1,1)
    x2=int(x/20)*20
    y2=int(y/10)*10
    yx=min(y2+10,len(mp.bit))
    for i in range(y2,yx):
        for j in range(x2,min(x2+20,len(mp.bit[i]))):
            tp=mp.bit[i][j]
            aired=tp in[0,1,8,10] or (i>0 and mp.bit[i-1][j]in[0,1,8]) or (i<len(mp.bit)-1 and mp.bit[i+1][j]in[0,1,8]) or (j>0 and mp.bit[i][j-1]in[0,1,8]) or (j<len(mp.bit[i])-1 and mp.bit[i][j+1]in[0,1,8])
            if aired:
                rect(j*10-dx,i*10-dy,10,10,nts[tp].col)
            else:
                rect(j*10-dx,i*10-dy,10,10,(0,0,0))
    #DONT DELETE
    p.dr(p.x,p.y)
    # for i in bobs:
    #     i.disp((i.y,i.x))
def getSave():
    global mp
    b=""
    print("\033c")
    with open("saveus/save.pile","r")as sv:
        b=sv.readlines()[0].replace("\n","")
    evald=eval(piler.dec(b))
    mp.bit=evald[0]
    p.hold=[[eval(j) for j in i]for i in evald[1]]
    p.x,p.y=evald[2]
    mp.datar()
def writSave():
    global mp
    rs=[[repr(j)for j in i]for i in p.hold]
    with open("saveus/save.pile","w")as sv:
        sv.write(piler.enc([mp.bit,rs,(p.x,p.y)]))#piler.enc
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
up,right,down,left,save,w,a,s,d,place,brek,inv,open=pygame.K_UP,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_LEFT,pygame.K_u,pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_p,pygame.K_b,pygame.K_i,pygame.K_o
while True:
        scrn.fill((255,255,255))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                quit()
            elif i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    kd=True
            #DONT DELETE
            # if i.key==py.K_LSHIFT:# and br.ys<3:
            #     br.ys+=1
        keys=pygame.key.get_pressed()
        do=""
        if keys[up]or keys[w]:
            do="z"
        elif keys[right]or keys[d]:
            do="x"
        elif keys[down]or keys[s]:
            do="c"
        elif keys[left]or keys[a]:
            do="v"
        p.mover(do)
        # print(do)
        # sleep(0.1)
        clk.tick(10)
        pr(p.x,p.y)
        scrn.blit(font.render(f"{do},", True, (255, 255, 255)),(0,0))
        pygame.display.flip()
while not True:
    fps.run()
    prat("fps: "+str(fps.getCur())+"          ",1,12)
    # if dpt.run():
    for i in bobs:
        i.run(mp.bit,[],p)
    p.mover(do)
    # move(0,12)
    # if rkt.run():
    sleep(0.1)
    #wasd/arrow-move
    #u-save
    #p-place
    #b-break
    #i-inve
    #o-open chest
    prat("Use arrow keys and wasd  to move. \"i\" to open your inventory. \"o\" to open the chest in front of you. \"u\" to save. \"b\" breaks the block in front of you, along with holding down an arrow key. Use number keys 1-5 to change your selected hotbar. \"p\" places the current selected block in front of you. \"o\" opens a chest in front of you.",1,13)
    print(m)
    do=keyboard.read_key()
    if do=="":
        continue
    if do=="t":
        texter()
        continue
    t2=time.time()
    if t2-ts<7 and do==pk[-1]:
        if pk[-2]==pk[-3] and pk[-4]==do:# and pk[-3]==pk[-4]
            do="b"
        else:
            pk.append(do)
            continue
    pk.append(do)
    if dev:
        prat(str(t2-ts)+str(randint(0,10)),1,16)
    ts=t2
    prat(do,1,15)
    
    if do == "up" or do == "w":
        do="z"
    elif do == "right" or do == "d":
        do="x"
    elif do == "down" or do == "s":
        do="c"
    elif do == "left" or do == "a":
        do="v"
    elif do=="u":
        writSave()
    