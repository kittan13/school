class Person(object):

    ##############################
    #コンストラクタといい、classの初期化のイメージ
    def __init__(self,name):
        self.name = name
    ######################################

    def say(self):
        print("I am{}. Hello".format(self.name))
        self.run(5)

    def run(self, num):
        print("run"* num)

    ##################################
    #デストラクタといい、必要なくなれば実行される。
    def __del__(self):
        print("good bye")
    ########################################3

person = Person("Mike")
person.say()

del person

print("###############")