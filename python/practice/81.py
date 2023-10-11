#クラスの継承

#classを定義して、何も実行しない場合はpass
#継承する側のclassには引数を(object)ではなく、(対象のクラス名)



class Car(object):
    def run(self):
        print("run")

class Toyota_Car(Car):
    pass

class Tetola_Car(Car):
    def auto_run(self):
        print("auto run")

car = Car()
car.run()

toyota_car = Toyota_Car()
toyota_car.run()

tetola_car = Tetola_Car()
tetola_car.auto_run()


class Cal(object):
    def sum(self,a):
        a += 1
        return a
    

class Cal_2(Cal):
    def sub(self,b):
        b -= 1
        return b
    

cal = Cal()
cal_2 = Cal_2()

print(cal.sum(5))
print(cal_2.sub(5))
