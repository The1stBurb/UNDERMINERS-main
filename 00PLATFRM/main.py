import pygame
from math import ceil
from time import time
pygame.init()
X = 1000
Y = 1000
scrn,clk=pygame.display.set_mode((X, Y)),pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
sz=60
grass=pygame.transform.scale(pygame.image.load("00PLATFRM\\imgs\\grass.png").convert_alpha(),(sz,sz))
rock=pygame.transform.scale(pygame.image.load("images\\rock_base.png").convert_alpha(),(sz,sz))
# block=pygame.transform.scale(pygame.image.load("00PLATFRM\\imgs\\block.png").convert_alpha(),(sz,sz))
# block_top=pygame.transform.scale(pygame.image.load("00PLATFRM\\imgs\\block_top.png").convert_alpha(),(sz,sz))
solids=[grass,rock]
quilt=[[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, -1], [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 
-1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
# for i in range(ceil(Y/sz)):
#     quilt.append([])
#     for j in range(ceil(X/sz)):
#         quilt[-1].append(-1)
quilt2=[]
solid=0
def image(img,x,y):
    scrn.blit(img,(x,y))
def rect(x,y,w,h,col=(255,255,255)):
    # print(col)
    pygame.draw.rect(scrn, col, pygame.Rect(x, y, w, h))
def text(txt,x,y,col=(0,0,0)):
    scrn.blit(font.render(txt, True, col),(x,y))
right,left=pygame.K_RIGHT,pygame.K_LEFT
late=time()
while True:
    scrn.fill((255,255,255))
    mse=pygame.mouse.get_pos()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print(quilt)
            quit()
        elif i.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            mx//=sz
            my//=sz
            mice=pygame.mouse.get_pressed()
            if mice[0]:
                quilt[my][mx]=solid
            elif mice[2]:
                quilt[my][mx]=-1
            
    keys=pygame.key.get_pressed()
    if time()-late>0.1:
        if keys[right] and solid<len(solids)-1:
            solid+=1
        elif keys[left] and solid>0:
            solid-=1
        late=time()
    rect(solid*(sz+10),920,sz+10,80,col=(200,200,200))
    for a,i in enumerate(solids):
        image(i,a*(sz+10),930)
    # for i in quilt2:
    #     image(solids[i[2]],i[0]*sz,i[1]*sz)
    for a,i in enumerate(quilt):
        for b,j in enumerate(i):
            if j==-1:
                continue
            image(solids[j],b*sz,a*sz)
    # for i in brcks:
    #     image(blcks[i[2]],i[0],i[1])
    image(solids[solid],(mse[0]//sz)*sz,(mse[1]//sz)*sz)
    clk.tick(60)
    pygame.display.flip()