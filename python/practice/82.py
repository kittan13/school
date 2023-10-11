########################################################
#メッソドのオーバーライドとsuperによる親のメソッドの呼び出し#
########################################################

#メゾットの場合「.」で呼び出すことができたが、class変数の場合でも「.」で呼び出すことができる。
#もし親のclass変数を使う場合、例えばanimal = Animal()とする際に、animal = Animal("〇〇")　と引数を指定上げることが必要。
#これは、子classは指定しなくても親クラスのメゾットを継承ためである。
#子クラスでも新たに行う場合、新しくメゾットを作ってあげればよい。(親のメゾットと同じ名前で)
#しかし、その場合、同じ処理を何機も書かなくてはいけない場合があるかもしれないが、super()を使うことで親のメゾットを呼び出すことができる。

class Animal(object):
    def __init__(self,name=None, color = "White"):
        self.name = name
        self.color = color

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name=name, color=color)

animal = Animal()
cat = Cat(name="Tama",color="green")

print(animal.name)
print(cat.name,cat.color)

"""
class animal(object):
    def __init__(self, name = None,color = 'white'):
        self.name = name
        self.height = 100
        self.color = color
 
class Cat(animal):
    def __init__(self,color,name,func):
        super().__init__(name = name, color = color)
        self.func = func
 
A = animal()
print(A.name,A.height,A.color)
 
B = Cat(func = 'nya', name = 'tama',color = 'black')
print(B.name,B.height,B.func,B.color)
"""