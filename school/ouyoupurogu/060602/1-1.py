import math

print(f'{"n":3}{"nの2乗":8}{"2のn乗":12}{"nの階乗":20}{"nのn乗":45}')

for n in range(1,21):   
    print(f'{n:3}{n**2:4}{2**n:8}{math.factorial(n):20}{n**n:28}')

