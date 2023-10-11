def sum_1(a,b):
    def sum_2 (c,d):
        return a + b +c + d
    return sum_2

cal_1 = sum_1(2,3)
cal_2 = sum_1(5,6)

print(cal_1(3,4))
print(cal_2(7,8))