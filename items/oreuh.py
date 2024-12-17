# no_rock=" "
# rock="◻"
# dark_rock="█"
# charium_ore="≈"
# nevelium_ore="¤"
# decante_ore="⋇"
# charcor_ore="◘"
# placed_rock=" "
from base_funcs import prat,intput,gtInt,itm
from bobs import xny
# from zlooter import roll
from random import choice,randint
# from itemuh import *
from time import sleep,time
class brck:
    def __init__(self,nm,disp,sprd,num,pronc,mnLvl,col=(0,0,0)):#name,what is displayed,the spread of a section, the id/num of place in nts list, how to pronounce,what level it takes to mine
        self.nm=nm
        self.txt=disp
        self.spr=sprd
        self.idd=num
        self.pro=pronc
        self.ml=mnLvl
        self.ms=0
        self.col=col
        self.pcb=True
        self.atk=1
        # print(nm,disp,sprd,num,pronc)
        # quit()
    def __str__(self):
        return f"{self.txt}"#{self.col}{self.txt}{("\033[0m"if self.col!="" else "")}"
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
no_rock=no_rock52("no_rock"," ",10,0,"air",0,col=(200,200,200))
placed_rock=placed_rock52("placed_rock","_",0,1,"placed rock",1,col=(211,211,211))
rock=rock52("rock","%",-1,2,"rock",1,col=(100,100,100))#◻
dark_rock=dark_rock52("dark_rock","$",2,3,"dark rock",2,col=(27,27,27))#█
charium_ore=charium_ore52("charium_ore","=",7,4,"ch-arh-ee-um ore",3,col=(0,100,0))#≈
nevelium_ore=nevelium_ore52("nevelium_ore","o",5,5,"neh-vel-ee-um ore",3,col=(0,0,139))#
decante_ore=decante_ore52("decante_ore","⋇",3,6,"dee-cant ore",4,col=(128,128,0))
charcor_ore=charcor_ore52("charcor_ore","&",10,7,"ch-arh-kor ore",1,col=(139,0,0))#◘
#"\033[48;2;red;green;bluem"
void=brck("void"," ",0,8," ",1234567890,col=(255,255,255))

dirt=dirt52("dirt","@",15,9,"dirt",0,col=(88,57,39))

# chest=chest52("chest","C",1,10,"chest",0,[])
nts=[no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt]#,chest]
#no_rock:0,
# print(rock+dark_rock+placed_rock+charium_ore+nevelium_ore+decante_ore+charcor_ore)



#ITEMUH FILE HERE!!!!!!!!!!
class bify:
    def __init__(self,itms,ams):
        self.itms=itms
        self.ams=ams
        self.nd=[]
class held:
    def __init__(self,nm,idd2,ms,dmg,bfy=[["","","",{}]],col=(0,0,0)):#name of, id of,mine strength, attack damage
        self.nm,self.idd,self.id,self.ms,self.atk=nm,-1,idd2,ms,dmg
        self.col=col
        self.pcb=False
        self.tp="held"
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
        super().__init__(nm,idd2,ms,dmg,col=rock.col)
        self.bfy=[itm(rock,5)]
        self.tp="pick"
        #rrr
        # r
        # r
    # def __init__(idd2,ms):
class charcor_pick52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=charcor_ore.col)
        self.bfy=[itm(charcor_ore,3),itm(rock,2)]
        self.tp="pick"
class charium_pick52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=charium_ore.col)
        self.bfy=[itm(charium_ore,3),itm(rock,2)]
        self.tp="pick"
class nevelium_pick52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=nevelium_ore.col)
        self.bfy=[itm(nevelium_ore,3),itm(rock,2)]
        self.tp="pick"
class sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=rock.col)
        self.bfy=[itm(rock,3)]
        self.tp="sword"
class charcor_sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=charcor_ore.col)
        self.bfy=[itm(charcor_ore,2),itm(rock,1)]
        self.tp="sword"
class charium_sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=charium_ore.col)
        self.bfy=[itm(charium_ore,2),itm(rock,1)]
        self.tp="sword"
class nevelium_sword52(held):
    def __init__(self, nm, idd2, ms, dmg):
        super().__init__(nm, idd2, ms, dmg,col=nevelium_ore.col)
        self.bfy=[itm(nevelium_ore,2),itm(rock,1)]
        self.tp="sword"
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