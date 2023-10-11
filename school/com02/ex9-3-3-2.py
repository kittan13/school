def EquilateralTriangle(a,b):
    return((a/4*(b**2)))
x=1.732
y=6
print("1辺の長さが"+str(y)+"の正三角形の面積は",end="")
print(str(round(EquilateralTriangle(x,y),2))+"である。")