# -*- cding: euc-jp -*-     #EUC


#ファイルの1行目、又は2行目tで文字コードを指定する。必要に応じて書き換え。
# -*- coding: utf-8 -*-    #ユニコード
# -*- coding: shift_jis -*-#シフトJIS

print("あいう")
print("5/3 =",5/3,"\nです")
print("5//3",5//3)

import math
print(8, 8**2, 2**8, math.factorial(8), 8**8)
"""
for n in range(1,11):
    print(n, n**2, 2**n, math.factorial(n), n**n)
"""

for n in range(1,21):
    print("{:3}{:4}{:8}{:20}{:28}".format(n, n**2, 2**n, math.factorial(n), n**n))

for n in [2,5,10,20]:
    print("{:3}{:4}{:8}{:20}{:28}".format(n, n**2, 2**n, math.factorial(n), n**n))
