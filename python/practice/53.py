""""
def  menu(**kwargs):
    #print(kwargs)
    for v,k in kwargs.items():
        print(v,k)
#menu(entree = "beef", drink = "tea")

d = {
    "entree":"beef",
    "drink":"tea",
    "dessert":"ice"
}

menu(**d)
"""

def menu(food,**kwarg,*arg):
    print(food)
    print(*arg)
    print(kwarg)

menu("banan",entree = "beef",drink ="ice","apple","orenge")