w ={"mon","tue","wed"}
f ={"apple","banana","orenge"}

d = {}
for x,y in zip(w,f):
    d[x] = y
print(d)

a ={x:y for x,y in zip(w,f)}
print(a)


a = {
    "x": 10,
    "y": 20,
    "z": 30
}
print(a)