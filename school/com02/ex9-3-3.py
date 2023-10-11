import math

def EquilateralTriangle(a):
    return((math.sqrt(3)/4*(a**2)))

x=6
print("各辺の長さが"+str(x)+"の正三角形の面積は",end="")
print(str(round(EquilateralTriangle(x),2))+"である。")