from random import randint,choice
# from zitemuh import hts
# from zoreuh import nts
resiz={"no_rock":0,"placed_rock":10,"rock":20,"dark_rock":30,"charium_ore":40,"nevelium_ore":50,"decante_ore":60,"charcor_ore":70,"void":80,"dirt":90,"chest":100,#no_rock,placed_rock,rock,dark_rock,charium_ore,nevelium_ore,decante_ore,charcor_ore,void,dirt,chest
"pick":1,"charcor_pick":11,"nevelium_pick":21,"sword":31,"charcor_sword":41,"charium_sword":51,"charium_sword":61,"nevelium_sword":71,"":81,"":91,"":101}#pick,charcor_pick,nevelium_pick,sword,charcor_sword,charium_sword,nevelium_sword
dat=[]
with open("Loot/loot.txt")as lt:
    # print(lt.readlines()[1:])
    dat=lt.read().split("\n")[1:]
stuffs=[]
for i in dat:
    # print(i)
    d=i.split(" ")
    # print(d,d[0][:-1])
    ran=d[2].split("-")
    # print("id:",resiz[d[0][:-1]],"Percent:",int(d[1][:-2]),"Range:",ran[0],"-",ran[1])
    stuffs.append([resiz[d[0][:-1]],int(d[1][:-2]),[int(ran[0]),int(ran[1])]])
def gitStf():
    return stuffs

    return rolled
    # roll2=[]
    # for i in rolled:
    #     if str(i[0])[-1]=="0":
    #         roll2.append([nts[int(i[0]/10)],i[1]])
    #     else:
    #         roll2.append([hts[int(i[0]/10)],i[1]])
    # return roll2
# r=roll()
# for i in r:
#     print(i[0].nm,i[1])