import math

print(math.log(8, 2))
print(math.log(625, 5))
print(math.log(1000, 10))

assert math.log(8, 2) == 3
assert math.log(625, 5) == 4
assert round(math.log(1000, 10)) == 3

def log(x, base):
    n = base
    i = 1
    while n * base <= x:
        n *= base
        i += 1
    return i

print(log(8, 2))
print(log(625, 5))
print(log(1000, 10))

assert log(8, 2) == 3
assert log(625, 5) == 4
assert log(1000, 10) == 3