import math

def logarithm(x, base):
    if x == 1:
        return 0

    left = 0
    right = x
    epsilon = 1e-7 # small value (precision of the result)
    
    m = (right + left) // 2 # middle
    
    while right - left > epsilon:

        if x <= base**m:
            right = m
        else:
            left = m

        m = (left + right) / 2

    return round(m, 7)

print(logarithm(8, 2))
print(logarithm(625, 5))
print(logarithm(1000, 10))

assert logarithm(8, 2)      == 3 == math.log(8, 2)
assert logarithm(625, 5)    == 4 == math.log(625, 5)
assert logarithm(1000, 10)  == 3 == round(math.log(1000, 10))