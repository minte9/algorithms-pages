""" Generate a list of prime numbers from 2 to 100.  
    Prime numbers are natural numbers greater than 1 that is not a product of two smaller natural numbers.  

    The first 25 prime numbers are: 
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 

    Make a slow version and a faster version of the function.  
"""


""" Loop through all elements has O(n^2) complexity.
    Since we call is_prime(n) inside a loop, the complexity is:
        O(n) x O(n) = O(n^2)
    This is very slow for large numbers.
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = set()
for x in range(2, 100):
    if is_prime(x):
        prime_numbers.add(x)

assert len(prime_numbers) == 25
print(prime_numbers)


""" A better version is to check divisibility only up to sqrt(n)
    The reduce the complexity to O(n * sqrt(n))
"""
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # +1 To include the square root itself
        if n % i == 0:
            return False
    return True

prime_numbers = {x for x in range(2, 100) if is_prime(x)}  # Set comprehension (faster than the loop/add)
assert len(prime_numbers) == 25
print(prime_numbers)