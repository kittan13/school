def Trapezium(a,b,c):
    return((a+b)*c*(1/2))

x=10
y=20
z=6
print("上底の長さが"+str(x)+"、下底の長さが"+str(y)+"、高さが"+str(z)+"の台形の面積は、",end="")
print(str(Trapezium(x,y,z))+"である。")