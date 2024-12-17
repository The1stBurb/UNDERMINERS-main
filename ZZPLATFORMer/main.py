import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Block size
sz = 20

# Player size
psz = 20

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Collision Detection")

# Sample map (0 = air, 1-3 = different block types)
game_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 2, 2, 0, 0],
    [1, 1, 1, 1, 0, 0, 2, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 3, 0, 0, 1, 1, 0, 0],
    [0, 0, 3, 3, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = psz
        self.speed = 2
        self.colliding = [False]
        self.g=0

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.size))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.size))
        if self.y>=SCREEN_HEIGHT-self.size:
            self.g=0

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.size, self.size))

    def check_collision(self, game_map):
        corners = [
            (self.x, self.y),
            (self.x + self.size, self.y),
            (self.x, self.y + self.size),
            (self.x + self.size, self.y + self.size)
        ]
        # if self.colliding[0]==True:
        for corner in corners:
            map_x = int(corner[0] // sz)
            map_y = int(corner[1] // sz)
            if 0 <= map_x < len(game_map[0]) and 0 <= map_y < len(game_map):
                if game_map[map_y][map_x] != 0:
                    self.colliding = [True,(map_x+0.5)*sz,(map_y+0.5)*sz,corner[0],corner[1]]
                    return
        self.colliding = [False]

def draw_map(surface):
    for y, row in enumerate(game_map):
        for x, block in enumerate(row):
            if block != 0:
                color = RED if block == 1 else GREEN if block == 2 else BLUE
                pygame.draw.rect(surface, color, (x * sz, y * sz, sz, sz))

# Create pl
pl = Player(0, 0)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    # pl.g = (keys[pygame.K_DOWN] - keys[pygame.K_UP])*2
    if keys[pygame.K_UP] and pl.g==0:
        pl.g=-3
    if pl.g<1:
        pl.g+=0.1
    pl.move(dx, pl.g)
    
    pl.check_collision(game_map)
    
    screen.fill(BLACK)
    draw_map(screen)
    pl.draw(screen)
    
    pc=pl.colliding
    if pc[0]:
        font = pygame.font.Font(None, 36)
        # text = font.render(f"Collision Detected!{pc},{pl.x//sz},{pl.y//sz}", True, WHITE)
        # screen.blit(text, (0, 10))
        bx,by=pc[1],pc[2]#*sz,pc[2]*sz
        px,py=pl.x,pl.y#pc[3],pc[4]
        if abs(px-bx)>abs(py-by):
            if px>bx:
                # pl.x=pc[3]
                pl.x-=dx*2-0.01
            elif px<bx:
                # pl.x=pc[4]#bx-sz
                pl.x-=dx*2+0.01
        elif abs(px-bx)<abs(py-by):
            if py>by:
                pl.y-=(pl.g*2-0.01)
            elif py<by:
                pl.y-=(pl.g*2+0.01)
                pl.g=0
        else:
            pl.y-=pl.g*2
            pl.x-=dx*2
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
