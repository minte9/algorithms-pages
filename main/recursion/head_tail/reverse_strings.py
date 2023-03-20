""" Reverse strings
Head tail technique

Another classic reverse algorithm, even though the 
iterative solution is better.

Base case: zero or one-character string
Argument passed: tail of the original string, with one less char
Argument closer to the base: array shrinks by one element
"""

# Recursive
def rrev(s):
    if len(s) == 0 or len(s) == 1:
        return s
    head = s[0]
    tail = s[1:]
    return rrev(tail) + head

# Iterative
def irev(s):
    rs = ''
    m = len(s)
    for i in range(1, m+1):
        rs += s[m - i]
    return rs


# Tests
assert rrev('S') == 'S'
assert rrev('XY') == 'YX'
assert rrev('CAT') == 'TAC'
assert rrev('Hello World!') == '!dlroW olleH'

assert irev('S') == 'S'
assert irev('XY') == 'YX'
assert irev('CAT') == 'TAC'
assert irev('Hello World!') == '!dlroW olleH'

# Overflow
try:
    rrev('a' * 1000)
except RecursionError as e:
    print(e) # maximum recursion depth exceeded