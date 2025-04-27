import math

def func(a, b, c):
    if c % a == 0 or c % b == 0:
        return math.floor((b-a) / c) + 1
    elif c % a == 0 and c % b == 0:
        return math.floor((b-a) / c) + 2
    return math.floor((b-a) / c)

print (func(1, 10, 3))
print (func(1, 9, 3))
print (func(3, 9, 3))