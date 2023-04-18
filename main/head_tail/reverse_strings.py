""" Reverse strings / Head tail technique
A classic reverse algorithm, even though the 
iterative solution is better.
"""

def head_tail_reverse(s):
    if len(s) <= 1: # Base case
        return s
    head = s[0]
    tail = s[1:]
    res  = head_tail_reverse(tail) + head # Recursive case
    return res

def reverse(str):
    m = len(str)
    s = ""
    for i in range(1, m + 1):
        s += str[m - i]
    return s

assert head_tail_reverse('S') == 'S'
assert head_tail_reverse('XY') == 'YX'
assert head_tail_reverse('CAT') == 'TAC'
assert head_tail_reverse('Hello World!') == '!dlroW olleH'
assert reverse('S') == 'S'
assert reverse('XY') == 'YX'
assert reverse('CAT') == 'TAC'
assert reverse('Hello World!') == '!dlroW olleH'

# Overflow
try:
    head_tail_reverse('a' * 1000)
except RecursionError as e:
    print(e) # maximum recursion depth exceeded

str = reverse('a' * 1000)
print(str)