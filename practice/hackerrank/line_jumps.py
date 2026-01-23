"""
    We have two kangaroos ready to jump in the same direction (positive infinity).
    They may start at different position (x) and can have different speed (v).
    Given the input (x1, v1, x2, v2) the function return YES or NO.
    If they can the end point in the same time, return YES.
    Position is in interval 0 - 10000
    Speed is in interval 1 - 10000
"""

def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return True
    return False

assert kangaroo(2, 1, 1, 2) == True
assert kangaroo(0, 3, 4, 2) == True
assert kangaroo(0, 2, 5, 3) == False
assert kangaroo(4523, 8092, 9419, 8076) == True