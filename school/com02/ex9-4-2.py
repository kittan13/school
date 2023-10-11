def StraightLine(a,b,c):
    return((-b+(b**2-4*a*c)**0.5)/2*a)

a=1
b=3
c=2

D=(b**2-4*a*c)**0.5

print("y="+str(a)+"x^2+"+str(b)+"x+"+str(c)+"の時、",end="")
if (D>=0):
    print("xの値は、"+str(StraightLine(a,b,c))+"である。",end="")
else:
    print("この二次関数のxの値を実数で求めることはできない。")