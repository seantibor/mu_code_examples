import random
import hypotenuse as h

n_triangles = 1000000

triangles = [(random.randint(1,100),random.randint(1,100)) for _ in range(n_triangles)]

c_sides = [h.hypotenuse(a,b) for a,b in triangles]

print(c_sides[:10])