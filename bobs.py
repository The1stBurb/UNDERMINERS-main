from collections import deque
from base_funcs import prat,dist
from time import sleep
from math import sin,cos
from random import randint,choice
# from main import mp
def navigate_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start[1], start[0], [])])
    visited = set()

    while queue:
        x, y, path = queue.popleft()
        
        if (x, y) == end:
            for i in path:
                # for j in i:
                prat("*",i[1]+1,i[0]+1)
            # prat("",0,18)
            # input()
            return path + [(x, y)]
        
        if (x, y) in visited or maze[x][y] != 0:
            continue
        
        visited.add((x, y))
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                queue.append((nx, ny, path + [(x, y)]))
    
    return None  # No path found

class xny:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x}, {self.y}"
class bob:
    def __init__(self,x,y,nm,tp,atk,sp):
        self.nm,self.tp,self.atk,self.sp,self.x,self.y=nm,tp,atk,sp,x,y
        self.s,self.t,self.path=0,xny(self.x,self.y),[]
        self.avp=[]
    def disp(self,d):
        prat(" ",self.x+1,self.y+1)#nots[mapd[self.y][self.x]]
        print()
        self.y,self.x=d
        prat(self.tp if self.path!=None and len(self.path)>1 else "O",self.x+1,self.y+1)
        print()
    def mve(self,mapd,nots,pr):
        # global mp
        if self.path==None:
            return "newPath"
        if len(self.path)<=1:
            self.path=navigate_maze(mapd,(self.x,self.y),(self.t.x,self.t.y))
            self.s=self.sp+1    
            return "startPath"
        d=self.path[0]
        if int(self.x/10)==int(pr.x/10) and int(self.y/10)==int(pr.y/10):
            self.disp(d)
        self.path.remove(d)
        return ""
        # self.disp(d)
        # return "newPath"
    def getTarget(self,pr,mapd):
        if dist(self.x,self.y,pr.x,pr.y)<=10:
            self.t.x=pr.x
            self.t.y=pr.y
        else:
            # a=randint(0,360)
            # # self.t.x,self.t.y=int(self.x+sin(a)*3),int(self.y-cos(a)*3)
            # self.t.x,self.t.y=self.x+randint(-2,2),self.y+randint(-2,2)
            # if self.t.y<0:
            #     self.t.y=0
            # elif self.t.y>len(mapd)-1:
            #     self.t.y=len(mapd)-1
            # if self.t.x<0:
            #     self.t.x=0
            # elif self.t.x>len(mapd[self.t.y])-1:
            #     self.t.x=len(mapd[self.t.y])-1
            # prat(self.t,1,20)
            self.t.x,self.t.y=choice(self.avp)
            prat(self.t,1,16)
        if self.t.x!=self.x and self.t.y!=self.y:
            self.path=[]
    def run(self,mapd,nots,pr):
        if self.avp==[]:
            for a,i in enumerate(mapd):
                for b,j in enumerate(i):
                    if j==0:
                        self.avp.append((b,a))
        if int(self.x/10)==int(pr.x/10) and int(self.y/10)==int(pr.y/10):
            self.disp((self.y,self.x))
        self.s+=1
        if self.path!=None and len(self.path)<=1:#dist(self.x,self.y,self.t.x,self.t.y)
            self.t.x,self.t.y=-1,-1
            # prat("as",0,17)
            self.getTarget(pr,mapd)
        if self.s>self.sp:
            # prat(str(len(self.path if self.path!=None else []))+" "*50,0,21)
            self.s=0
            dec=self.mve(mapd,nots,pr)
            # self.disp((self.y,self.x))
            if dec=="newPath":
                self.getTarget(pr,mapd)
trol=bob(2,9,"Troll","N",5,1)
bobs=[]
# for i in range(0,360,6):
#     prat(f"{i},{sin(i)}",10,10)
#     prat("@",int(10+sin(i)*5),int(10+cos(i)*5))

# # Example usage
# mp = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0]
# ]

# start = (0, 0)
# end = (4, 4)

# path = navigate_maze(mp, start, end)

# # if path:
# #     print("Path found:", path)
# # else:
# #     print("No path found")

# # Visualize the path
# if path:
#     for i, row in enumerate(mp):
#         for j, cell in enumerate(row):
#             if (i, j) in path:
#                 print("*", end=" ")
#             else:
#                 print(cell, end=" ")
#         print()
# while True:
#     trol.run()
#     sleep(0.1)