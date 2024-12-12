#this will run saving ig!
cows=[
    # 0   1   2   3   4   5   6   7
    ["a","b","c","d","e","f","0","6"],#0
    ["g","h","i","j","k","l","1","7"],#1
    ["m","n","o","p","q","r","2","8"],#2
    ["s","t","u","v","w","x","3","9"],#3
    ["y","z",",","[","]","(","4","'"],#4
    [")",".","\""," ","A","B","5","C"],#5
    ]
#0-060 air
#1-061 placed_rock
#2-062 rock
#3-063 dark_rock
#4-064 charium
#5-065 nevelium
#6-070 decante
#7-071 charcor
#8-072 void
#9-073 dirt
#10-061060 chest
def gcow(txtId):
    for a,j in enumerate(cows):
        for b,k in enumerate(j):
            if k in txtId:
                return b,a
    print(txtId)
    # return -1,-1
def enc(txt):
    cid2=""
    for i in str(txt):
        cid=("0"if i.lower()==i else "1")
        js=gcow(i.lower())
        cid+=(str(js[0])+str(js[1]))
        # print(cid)
        cid2+=cid
    return cid2
def dec(txt):
    wrd=""
    for i in range(0,len(txt),3):
        cpl=txt[i]
        xcd=int(txt[i+1])
        ycd=int(txt[i+2])
        cow=cows[ycd][xcd]
        wrd+=(cow if cpl=="0"else cow.upper())
        # print(cpl+str(xcd)+str(ycd))
    return wrd
def saver(txt="dec"):
    if txt=="dec":
        gt=""
        with open("save.pile","r")as sp:
            gt=sp.read()
        return dec(gt)
    else:
        with open("save.pile","w")as sp:
            sp.write(enc(txt))