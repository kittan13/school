num = input("数字を入力してください:")
print(str(num)+"は、",end="")
if(int(num)%2)!=0:
    print("奇数",end="")
else:
    print("偶数",end="")

print("です。\n")