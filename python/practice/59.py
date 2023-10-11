def greeding():
    yield "Good Morning"
    yield "Good afternoon"
    yield "Good night"

g = greeding()
print(next(g))
print(next(g))
print("a")
print(next(g))