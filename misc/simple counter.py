x1 = 1
x2 = 1

print(x1)
print(x2)
for i in range(10000000):
    x1, x2 = x2, x1+x2

print(x2)
print('digits', len(str(x2)))
