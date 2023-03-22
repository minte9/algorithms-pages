""" Palindrome strings

A palindrome is a word or phrase that is spelled the same 
when written forward or backword (level, race car)
Will split the string into head, middle, tail.

Base case: zero or one-character string
Argument passed: middle of the string
Approach to the base: argument shrinks by two chars
"""

# Recursive
def rIsPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    first = s[0]
    last = s[-1]
    middle = s[1:-1]
    return first == last and rIsPalindrome(middle)

# Iterative
def iIsPalindrome(s):
    m = len(s)
    for i in range(0, m):
        first = s[i]
        last = s[-1-i]
        if first != last:
            return False
    return True

# Tests
assert rIsPalindrome('level')
assert rIsPalindrome('rac e car')
assert not rIsPalindrome('levels')
assert not rIsPalindrome('race car')

assert iIsPalindrome('level')
assert iIsPalindrome('rac e car')
assert not iIsPalindrome('levels')
assert not iIsPalindrome('race car')
