while True:					#◀◀ 1行目は字下げせず左端
	name=input("名前？:")		#◀◀ TABキーでインデント
	number=eval(input("回数？:"))
	for i in range(number):	#◀◀ インデント2段目
		if i%3==0:				#◀◀ インデント3段目
			print("Hello, %s." % name)	#◀◀ インデント4段目
		elif i%3==1:		#◀◀ インデントを戻し3段目
			print("\tHey, %s!" % name)	#◀◀ インデント4段目
		else:				#◀◀ インデントを戻し3段目
			print("\t\tHello, World!!!")	#◀◀ インデント4段目