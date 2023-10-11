def StraightLine(a,b,c,d):
    return((c-d)/(a-b),c-((c-d)/(a-b))*a)

x_1=14
x_2=6
y_1=48
y_2=10
x=y_1-y_2/x_1-x_2
B=y_1-(y_1-y_2/x_1-x_2)*x_1
print("直線の傾きが"+str(x)+"切片が"+str(B)+"の一次関数は、",end="")
if (B>0):
        print("y="+str(round(StraightLine(x),2))+"x+"+str(StraightLine(B))+"である。")
else:
        print("y="+str((y_1-y_2)/(x_1-x_2))+"x"+str(y_1-((y_1-y_2)/(x_1-x_2))*x_1)+"である。")