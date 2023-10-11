input = int(input("西暦を入力してください。\n"))

if(input>=1868 and input<=1911):
    nengo = "明治"
    year = input - 1867
    if(year == 1):
        lastyear = input - 1864
        lastnengo ="慶応"
        print("西暦",input,"年は",nengo,year,"年です。\n",end="")
    else:
        print("西暦",input,"年は",nengo,year,"年です。\n",end="")

elif(input >= 1912 and input <= 1925):
    nengo="大正"
    year = input - 1911
    if(year == 1):
        lastyear = input -1867
        lastnengo="明治"
        print("西暦",input,"年は",nengo,"元年(",lastnengo,lastyear,"年)です。\n",end="")

    else:
        print("西暦",input,"年は",nengo,year,"年です。\n")

elif(input >= 1926 and input <= 1988):
    nengo ="昭和"
    year = input -1925
    if(year == 1):
        lastyear =input -1911
        lastnengo="大正"
        print("西暦",input,"年は",nengo,"元年(",lastnengo,lastyear,"年)です。\n",end="")

    else:
        print("西暦",input,"年は",nengo,year,"年です。\n")

elif(input >= 1989 and input <= 2018):
    nengo ="平成"
    year = input -1988
    if(year == 1):
        lastyear =input -1925
        lastnengo="昭和"
        print("西暦",input,"年は",nengo,"元年(",lastnengo,lastyear,"年)です。\n",end="")

    else:
        print("西暦",input,"年は",nengo,year,"年です。\n")

elif(input >= 2019):
    nengo ="令和"
    year = input -2018
    if(year == 1):
        lastyear =input -1988
        lastnengo="平成"
        print("西暦",input,"年は",nengo,"元年(",lastnengo,lastyear,"年)です。\n",end="")

    else:
        print("西暦",input,"年は",nengo,year,"年です。\n")

else:
    print("西暦",input,"年は、かなり古い時代です。\n",end="")


