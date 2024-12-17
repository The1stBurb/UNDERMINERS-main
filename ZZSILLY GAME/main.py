import pygame
pygame.init()
X = 1000
Y = 1000
scrn,clk=pygame.display.set_mode((X, Y)),pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
sz=60
top=pygame.transform.scale(pygame.image.load("ZZSILLY GAME\\images\\top.png").convert_alpha(),(sz,sz))
block=pygame.transform.scale(pygame.image.load("ZZSILLY GAME\\images\\block.png").convert_alpha(),(sz,sz))
brck=[(60,60),]#(90,75),(120,65),(57,85),(28,70)]
# , (28, 69)
#(120,65)
#123
#4 5
#678
sc_top=[
(-60,-5),#1
(30,15),#2
(3,-25),#3
(-30,10),#4
(30,-10),#5
(-3,25),#6
(-30,-15),#7
(60,5),#8
]
for i in sc:
    b=brck[0]
    brck.append((b[0]+i[0],b[1]+i[1]))
    # brck.append((b[0]-3,b[1]+25))
#1
#32
#to get 2 do 30 right, than 15 down
#to get 3 go 3 left than 25 down
def image(img,x,y):
    scrn.blit(img,(x,y))
while True:
    scrn.fill((255,255,255))
    mse=pygame.mouse.get_pos()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print(brck)
            quit()
        elif i.type==pygame.MOUSEBUTTONDOWN:
            brck.append((mse[0],mse[1]))
    for i in brck:
        image(top,i[0],i[1])
    image(top,mse[0],mse[1])
    clk.tick(60)
    pygame.display.flip()
