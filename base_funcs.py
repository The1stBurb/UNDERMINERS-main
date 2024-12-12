from math import sqrt
# import sys
import time
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))
def move(x, y):
    print(f"\033[{y};{x}H", end="")
def prat(txt,x,y):
    move(x,y)
    print(txt,end="")
#in range
def inr(n,mn,mx):
    return n>=mn and n<mx
#gets the diectionr based on a num
def gd(n):
    if n==0:#up
        return [0,-1]
    elif n==1:#right
        return [1,0]
    elif n==2:#down
        return [0,1]
    elif n==3:#left
        return [-1,0]
def exli(thng,num):
    return [thng for i in range(num)]
def intput(*txt):
    s=""
    for i in txt:
        s+=str(i)+" "
    return input(s+"\n >> ")
def gtInt(inp,mn,mx):
    while True:
        n=intput(inp)
        if n.isdigit():
            if int(n)>=mn and int(n)<=mx:
                return int(n)
            else:
                print(f"It has to be within {mn} and {mx}!")
        else:
            print("That isn't an int! Try again!")
def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1+y2)**2)
# intput("Hasf","as",2)
class itm:
    def __init__(self,tp,amnt):
        self.tp=tp
        self.no=amnt
    def __str__(self):
        return f"{self.no}x {repr(self.tp)}"
    def __repr__(self):
        return f"itm({self.tp.nm},{self.no})"#__class__.__name__
# def calcfps(num_frames=100): 
#     fps_values = []
#     prev_frame_time = time.time()
    
#     for _ in range(num_frames):
#         # Simulate frame processing
#         # Replace this with your actual frame processing code
#         time.sleep(0.01)  # Simulating 10ms of processing time
        
#         new_frame_time = time.time()
#         fps = 1 / (new_frame_time - prev_frame_time)
#         fps_values.append(fps)
#         prev_frame_time = new_frame_time
    
#     avg_fps = sum(fps_values) / len(fps_values)
#     return round(avg_fps, 2)
class runTimer:
    def __init__(self,fps,speed=(1/60)):#strt,end,speed):
        # self.st,self.ed,self.sp=strt,end,speed
        self.fps,self.sp=fps,speed
        self.cc=0
    def run(self):
        self.cc+=1
        return self.cc>=self.fps
class calcFrm:
    def __init__(self):
        self.rn=time.time()
        self.pr=self.rn
        self.fpsv=[]
    def run(self):
        self.pr=self.rn
        self.rn=time.time()
        self.fpsv.append(1/(self.rn-self.pr+0.0001))
        if len(self.fpsv)>50:
            self.fpsv.pop(0)
    def getAvr(self):
        return round(sum(self.fpsv)/len(self.fpsv),2)
    def getCur(self):
        return round(self.fpsv[-1],2)
