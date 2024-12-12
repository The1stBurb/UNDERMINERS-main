from random import randint,seed,random
from math import cbrt,floor
class PerlinNoise:
    def __init__(self):
        self.permutation = [151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
        self.p = self.permutation * 2
        self.octaves = 4
        self.falloff = 0.5

    def noise(self, x, y=0, z=0):
        X = int(floor(x)) & 255
        Y = int(floor(y)) & 255
        Z = int(floor(z)) & 255
        x -= floor(x)
        y -= floor(y)
        z -= floor(z)
        u = self.fade(x)
        v = self.fade(y)
        w = self.fade(z)
        A = self.p[X]+Y
        AA = self.p[A]+Z
        AB = self.p[A+1]+Z
        B = self.p[X+1]+Y
        BA = self.p[B]+Z
        BB = self.p[B+1]+Z

        result = self.lerp(w, self.lerp(v, self.lerp(u, self.grad(self.p[AA], x, y, z),self.grad(self.p[BA], x-1, y, z)),self.lerp(u, self.grad(self.p[AB], x, y-1, z),self.grad(self.p[BB], x-1, y-1, z))),self.lerp(v, self.lerp(u, self.grad(self.p[AA+1], x, y, z-1),self.grad(self.p[BA+1], x-1, y, z-1)),self.lerp(u, self.grad(self.p[AB+1], x, y-1, z-1),self.grad(self.p[BB+1], x-1, y-1, z-1))))
        return (result + 1) / 2

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, t, a, b):
        return a + t * (b - a)

    def grad(self, hash, x, y, z):
        h = hash & 15
        u = x if h < 8 else y
        v = y if h < 4 else (x if h == 12 or h == 14 else z)
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

    def noise_detail(self, lod, falloff):
        self.octaves = lod
        self.falloff = falloff
def noise(x,y=0,z=0):
    return PerlinNoise().noise(x,y,z)
# Usage example
pn = PerlinNoise()
print(pn.noise(0.5, 0.5))  # 2D noise
print(pn.noise(0.5, 0.5, 0.5))  # 3D noise
seed(0)
def rnd(n,n2):
    return round(n*10**n2)/10**n2
def mp(n, start1, stop1, start2, stop2):
  return ((n-start1)/(stop1-start1))*(stop2-start2)+start2
def noise(x=0,y=0,z=0):
    n=randint(min(x,y),max(x,y))+random()
    n2=randint(min(y,z),max(y,z))+random()
    n3=randint(min(x,z),max(x,z))+random()
    nn=cbrt(n*n2*n3)
    return x,y,rnd(n,2),rnd(n2,2),rnd(n3,2),rnd(nn,2),rnd((n+n2+n3)/3,2),rnd(mp(nn,min(n,min(n2,n3)),max(n,max(n2,n3)),0,1),2)
nl="$8#hpZLYvr/)[_>I\"."#18, we need 11 or 0-10
nl="0123456789@"#11 ig
# for i in range(10):
#     for j in range(10):
#         n=int(noise(i,j)*10)
#         print(nl[n],end="")
#     print(n)
for i in range(5):
    for j in range(2):
        print(noise(i,j))