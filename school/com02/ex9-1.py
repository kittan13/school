def baisu(kazu,waru):
    print(str(kazu)+"は"+str(waru)+"の倍数",end="")
    if(kazu%waru==0):
        print("です。")
    else:
        print("ではありません。")

#いろいろな数が倍数か否かを調べましょう。
a=15

baisu(a,3)
baisu(10.5,5)

a +=10
baisu(a,10000)

a +=1
#baisu(a)