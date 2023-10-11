t = (1,2,3,4,5)
r = []

for i in t:
    if i%2 == 0:
        r.append(i)

print(r)

r = [i for i in t if i%2 ==0]
print(r)