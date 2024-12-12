import mouse
import sys
from base_funcs import prat
from time import sleep
from bobs import xny
class mos:
    def __init__(self):
        self.ix=0
        self.iy=0
        self.init()
    def get(self):
        gp=mouse.get_position()
        return [gp[0]-self.ix,gp[1]-self.iy]
    def init(self):
        print("\033c",end="")
        # print("asdlkjandskgksa")
        print("#  CLICK ON THE HASH with the LEFT button! If you do not the game will not WORK",1,1)
        while self.ix==0 and self.iy==0:
            sleep(0.1)
            if mouse.is_pressed():
                got=self.get()
                self.ix=got[0]
                self.iy=got[1]
    def __str__(self):
        g=self.get()
        return f"{round(g[0])},{round(g[1])}"
m=mos()
# m.init()
print("\033c",end="")
print("1234567890")
for i in range(2,10):
    print(i)
print("0")
while True:
    print("\033c")
    prat(m,1,3)
    print("w")
    # print("#")
    sleep(0.1)