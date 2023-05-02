""" Palindrome / First last middle technique

A palindrome is a word or phrase that is spelled the same 
when written forward or backword (level, race car).
The iterative technique is better!
"""

def isPalindrome_recursive(s):
    if len(s) <= 1: # Base case
        return True

    first = s[0]
    last = s[-1]
    middle = s[1:-1]
    if first == last:
        return isPalindrome_recursive(middle) # Recursive

    return False

def isPalindrome_iterative(s):
    m = len(s)
    for i in range(0, m):
        first = s[i]
        last  = s[m-1-i]
        if first != last:
            return False
            
    return True

assert isPalindrome_recursive('level')  == True
assert isPalindrome_recursive('rac e car') == True
assert isPalindrome_recursive('levels') == False
assert isPalindrome_recursive('race car') == False
assert isPalindrome_iterative('level') == True
assert isPalindrome_iterative('rac e car') == True
assert isPalindrome_iterative('levels') == False
assert isPalindrome_iterative('race car') == False