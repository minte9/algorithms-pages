""" Reverse strings / Head tail technique
A classic recursive algorithm, even though 
the iterative solution is better.
"""

def reverse_string_recursive(str):
    if len(str) <= 1: # Base case
        return str
    head = str[0]
    tail = str[1:]
    res  = reverse_string_recursive(tail) + head
    return res

def reverse_string_iterative(str):
    m = len(str)
    s = ""
    for i in range(1, m + 1):
        s += str[m - i]
    return s

assert reverse_string_recursive('S') == 'S'
assert reverse_string_recursive('XY') == 'YX'
assert reverse_string_recursive('CAT') == 'TAC'
assert reverse_string_recursive('Hello World!') == '!dlroW olleH'
assert reverse_string_iterative('S') == 'S'
assert reverse_string_iterative('XY') == 'YX'
assert reverse_string_iterative('CAT') == 'TAC'
assert reverse_string_iterative('Hello World!') == '!dlroW olleH'

# Overflow
try:
    reverse_string_recursive('a' * 1000)
except RecursionError as e:
    print(e) # maximum recursion depth exceeded

str = reverse_string_iterative('a' * 1000)
print(str)