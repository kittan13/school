def sum(a):
    a += 1
    return a

def sub(b):
    b = b + 5
    return b

print(sum(5))
print(sub(5))


#################################################

class Cal(object):
    def sum_2(self,a):
        a += 100
        return a

    def sub_2(self,b):
        b = b + 1000
        return b


##ここで引数込みでcalに入れているため、基となる引数は(self,a)で二つ用意しないといけない。
cal = Cal()
print(cal.sum_2(5))
print(cal.sub_2(5))

#####################################################


class Cal_3(object):
    def sum_3(a):
        a += 10000
        return a

    def sub_3(b):
        b = b + 100000
        return b

print(Cal_3.sum_3(5))
print(Cal_3.sub_3(5))