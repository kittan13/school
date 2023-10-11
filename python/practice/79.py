class Person(object):
    def __init__(self,name):
        self.name = name

    def say(self):
        print("I am{}. Hello".format(self.name))
        self.run(5)

    def run(self, num):
        print("run"* num)

person = Person("Mike")
person.say()