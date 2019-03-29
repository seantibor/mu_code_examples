import random

results = [0,0]
for _ in range(10000000):
    results[random.randint(0,1)] += 1

print(results)
