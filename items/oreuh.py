# no_rock=" "
# rock="◻"
# dark_rock="█"
# charium_ore="≈"
# nevelium_ore="¤"
# decante_ore="⋇"
# charcor_ore="◘"
# placed_rock=" "
from base_funcs import prat,intput,gtInt,itm
# from zlooter import roll
from random import choice,randint
# from itemuh import *
from time import sleep,time
class brck:
    def __init__(self,nm,disp,sprd,num,pronc,mnLvl,col=""):#name,what is displayed,the spread of a section, the id/num of place in nts list, how to pronounce,what level it takes to mine
        self.nm=nm
        self.txt=disp
        self.spr=sprd
        self.idd=num
        self.pro=pronc
        self.ml=mnLvl
        self.ms=0
        self.col=col
        self.pcb=True
        # print(nm,disp,sprd,num,pronc)
        # quit()
    def __str__(self):
        return f"{self.col}{self.txt}{("\033[0m"if self.col!="" else "")}"
    def __repr__(self):
        return self.nm
    def stat(self):
        print(self.nm,str(self))
        print(" ",self.idd)
        print(" ",self.pro)
        print(" ",self.ml)
class no_rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class placed_rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class dark_rock52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class charium_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class nevelium_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class decante_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class charcor_ore52(brck):
    pass
    # def __init__(self,nm,disp,sprd):
    #     super().__init__(nm,disp,sprd)
class dirt52(brck):
    pass
class chest52(brck):
    def __init__(self,nm,disp,sprd,num,pronc,mnLvl,roleth):
        super().__init__(nm,disp,sprd,num,pronc,mnLvl,col="\033[48;2;119;69;19m")
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
        while True:
            print("\033c")
            p.prInv1()
            for b in range(3):
                prat(b+1,b*16+3,9)
            for a,i in enumerate(self.holds):
                prat(a+1,1,a+10)
                for b,j in enumerate(i):
                    prat("|"+str(j),b*16+3,a+10)
            print()
            if intput("Would you like to leave? (exit)")=="exit":
                print("Exiting...")
                return
            x1,y1,x2,y2=0,0,0,0
            flis=""
            flis2=""
            if ck:
                print("Click where you wish to move! You may have to click twice.")
                tms=time()
                while x1==0 or x2==0 or y1==0 or y2==0:
                    #ys-13,27,41,55,69,97
                    #     14 14 14 14 14
                    #xs-12,108,204,300,396
                    #     96  96  96  96
                    #ys-125,139,153
                    #xs-12,108,204
                    #MINUS 3 ALL X, MINUS 4 ALL Y
                    if not m.ip():
                        continue
                    sleep(0.5)
                    mp=m.get()
                    x=0
                    if mp.x>=8 and mp.x<105:
                        x=1
                    elif mp.x>=105 and mp.x<201:
                        x=2
                    elif mp.x>=201 and mp.x<297:
                        x=3
                    elif mp.x>=297 and mp.x<393:
                        x=4
                    elif mp.x>=393 and mp.x<393+96:
                        x=5
                    y=0
                    if mp.y>=9 and mp.y<23:
                        y=1
                    elif mp.y>=23 and mp.y<37:
                        y=2
                    elif mp.y>=37 and mp.y<51:
                        y=3
                    elif mp.y>=51 and mp.y<65:
                        y=4
                    elif mp.y>=65 and mp.y<79:
                        y=5
                    elif mp.y>=93 and mp.y<107:
                        y=6
                    elif mp.y>=121 and mp.y<135:
                        y=1
                    elif mp.y>=135 and mp.y<149:
                        y=2
                    elif mp.y>=149 and mp.y<163:
                        y=3
                    if x1==0 or y1==0:
                        if mp.y>=121:
                            flis="chest"
                        else:
                            flis="inv"
                        x1,y1=x,y
                        # if x1!=0 and y1!=0:
                        prat("\033[42m"+("|"+str((self.holds if flis=="chest"else p.hold)[y-1][x-1]))+"\033[0m",(x-1)*16+3,y+((1 if y!=6 else 2) if flis=="inv"else 9))
                        print("")
                        prat(f"{x},{y},{flis}",1,18)
                        print("")
                    else:
                        # if (flis=="chest" and y<121) or (flis=="inv" and y>=121):
                        if mp.y>=121:
                            flis2="chest"
                        else:
                            flis2="inv"
                        x2,y2,=x,y
                        # prat("yo    ",x*16+3,y+10)
                        # if x2!=0 and y2!=0:
                        prat("\033[42m"+("|"+str((self.holds if flis2=="chest"else p.hold)[y-1][x-1]))+"\033[0m",(x-1)*16+3,y+((1 if y!=6 else 2) if flis2=="inv"else 9))
                        print("")
                        prat(f"{x},{y},{flis2}",1,18)
                        print("")
                prat("",0,15)
            # print("\n",x1,y1,x2,y2)
            # input()
            # continue
            else: 
                flis=intput("Where is the first item? (inv,chest)")
                if flis!="inv" and flis!="chest":
                    continue
                # inor=intput("Is it into your inventory or into the chest? (inv,chest)")
                x1,y1=gtInt("What is the X coordinate of the item in "+("your inventory"if flis=="inv" else "the chest")+"?",1,(3 if flis=="chest" else 5)),gtInt("Whats the Y?",1,(3 if flis=="chest" else 6))
                prat("\033[42m"+("|"+str((self.holds if flis=="chest"else p.hold)[y1-1][x1-1]))+"\033[0m",(x1-1)*16+3,y1+((1 if y1!=6 else 2) if flis=="inv"else 9))
                print("")
                prat("",1,21)
                flis2=intput("Where is the second item? (inv,chest)")
                if flis2!="inv" and flis2!="chest":
                    continue
                x2,y2=gtInt("What is the X coordinate of where you want to move it"+(" into your inventory"if flis2=="inv" else " into the chest")+"?",1,(5 if flis2=="inv" else 3)),gtInt("What is the Y?",1,(6 if flis2=="inv" else 3))
                prat("\033[42m"+("|"+str((self.holds if flis2=="chest"else p.hold)[y2-1][x2-1]))+"\033[0m",(x2-1)*16+3,y2+((1 if y2!=6 else 2) if flis2=="inv"else 9))
                print("")
                prat("",1,27)
                # print(x1,y1,x2,y2)
            if intput("Is this right? (y/n)")=="n":
                continue
            it1=(self.holds if flis=="chest"else p.hold)[y1-1][x1-1]
            it2=(self.holds if flis2=="chest"else p.hold)[y2-1][x2-1]
            if it1.tp.nm==it2.tp.nm:
                it1.no+=it2.no
                it2=itm(void,0)
            if flis=="inv":
                p.hold[y1-1][x1-1]=it2
            else:
                self.holds[y1-1][x1-1]=it2
            if flis2=="inv":
                p.hold[y2-1][x2-1]=it1
            else:
                self.holds[y2-1][x2-1]=it1
    def brek(self,p):
        pass
no_rock=no_rock52("no_rock"," ",10,0,"air",0)
placed_rock=placed_rock52("placed_rock","_",0,1,"placed rock",1,col="\033[48;2;211;211;211m")
rock=rock52("rock","%",-1,2,"rock",1,col="\033[48;2;100;100;100m")#◻
dark_rock=dark_rock52("dark_rock","$",2,3,"dark rock",2,col="\033[48;2;27;27;27m")#█
charium_ore=charium_ore52("charium_ore","=",7,4,"ch-arh-ee-um ore",3,col="\033[48;2;0;100;0m")#≈
nevelium_ore=nevelium_ore52("nevelium_ore","o",5,5,"neh-vel-ee-um ore",3,col="\033[48;2;0;0;139m")#
decante_ore=decante_ore52("decante_ore","⋇",3,6,"dee-cant ore",4,col="\033[48;2;128;128;0m")
charcor_ore=charcor_ore52("charcor_ore","&",10,7,"ch-arh-kor ore",1,col="\033[48;2;139;0;0m")#◘
#"\033[48;2;red;green;bluem"
void=brck("void"," ",0,8," ",1234567890,col="\033[48;2;0;0;0m")

dirt=dirt52("dirt","@",15,9,"dirt",0,col="\033[48;2;88;57;39m")

chest=chest52("chest","C",1,10,"chest",0,[])
nts=[no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt,chest]
#no_rock:0,
# print(rock+dark_rock+placed_rock+charium_ore+nevelium_ore+decante_ore+charcor_ore)



#ITEMUH FILE HERE!!!!!!!!!!
class bify:
    def __init__(self,itms,ams):
        self.itms=itms
        self.ams=ams
        self.nd=[]
class held:
    def __init__(self,nm,idd2,ms,dmg,bfy=[["","","",{}]]):#name of, id of,mine strength, attack damage
        self.nm,self.idd,self.id,self.ms,self.dmg=nm,-1,idd2,ms,dmg
        self.col=""
        self.pcb=False
    def __str__(self):
        return self.nm
    def __repr__(self):
        return self.nm
    def crafty(self):
        print(self.nm)
        for i in self.bfy:
            print(" ",i)
class pick52(held):
    def __init__(self,nm,idd2,ms,dmg):
        super().__init__(nm,idd2,ms,dmg)
        self.bfy=[itm(rock,5)]
        #rrr
        # r
        # r
    # def __init__(idd2,ms):
class charcor_pick52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(charcor_ore,3),itm(rock,2)]
class charium_pick52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(charium_ore,3),itm(rock,2)]
class nevelium_pick52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(nevelium_ore,3),itm(rock,2)]
class sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(rock,3)]
class charcor_sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(charcor_ore,2),itm(rock,1)]
class charium_sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(charium_ore,2),itm(rock,1)]
class nevelium_sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg)
        self.bfy=[itm(nevelium_ore,2),itm(rock,1)]
pick=pick52("pick",0,1,1)
charcor_pick=charcor_pick52("charcor_pick",1,2,1)
nevelium_pick=nevelium_pick52("nevelium_pick",2,3,2)
burb=pick52("burb",-1,10,10)
sword=sword52("sword",3,0,3)
charcor_sword=charcor_sword52("charcor_sword",4,0,5)
charium_sword=charium_sword52("charium_sword",5,0,7)
nevelium_sword=nevelium_sword52("nevelium_sword",6,1,8)
# _sword=_sword52("",7,1,10)
hts=[pick,charcor_pick,nevelium_pick,sword,charcor_sword,charium_sword,nevelium_sword]
# class p:
#     def __init__(self):
#         self.hold=[
#             [itm(void,0),itm(dirt,5),itm(rock,5)],
#             [itm(dark_rock,3),itm(void,0),itm(void,0)]
#         ]
def craft(hav):
    has={}
    for a,i in enumerate(hav.hold):
        for b,j in enumerate(i):
            if j.tp.nm!="void":
                if j.tp.nm in has:
                    has[j.tp.nm].append([a,b,j])
                else:
                    has[j.tp.nm]=[[a,b,j]]
    # cbl=[]
    # for i in hts:
    #     for j in i.bfy:
    #         if j.tp.nm in has:
    #             for k in has[j.tp.nm]:
    #                 if k[2].no>=j.no:
    #                     cbl.append(i)
    htss={}
    for i in hts:
        i.crafty()
        htss[i.nm.lower()]=i
    buld=intput("What would you like to build?").lower()
    if not buld in htss:
        return
    for i in htss[buld].bfy:
        if i.tp.nm in has:
            for j in has[i.tp.nm]:
                if j[2].no<i.no:
                    return
    for i in htss[buld].bfy:
        if i.tp.nm in has:
            for j in has[i.tp.nm]:
                if j[2].no>=i.no:
                    hav.hold[j[0]][j[1]].no-=i.no
                    break
    hav.addItm(htss[buld])