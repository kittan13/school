import math

def Circle(r):
    return(math.pi*(r**2))

r=2
print("半径の長さが"+str(r)+"の円の面積は",end="")
print(str(round(Circle(r),2))+"である。")