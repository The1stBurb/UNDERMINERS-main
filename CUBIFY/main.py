import pygame
pygame.init()
X = 1000
Y = 1000
scrn,clk=pygame.display.set_mode((X, Y)),pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
sz=60
class brick:
    def __init__(self):#,x,y,z):
        pass
        # self.x,self.y,self.z=x,y,z
brcks=[
    [[brick(),brick(),],[brick(),brick(),],],
    [[brick(),brick(),],[brick(),brick(),],],
]
blck=pygame.transform.scale(pygame.image.load("CUBIFY\\cube.png").convert_alpha(),(sz,sz))
def image(img,x,y):
    scrn.blit(img,(x,y))
while True:
    scrn.fill((255,255,255))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
    for z,i in enumerate(brcks):
        for y,j in enumerate(i):
            for x,k in enumerate(j):
                image(blck,(1-x)*sz/2,(1-y)*sz/2)
    pygame.display.flip()