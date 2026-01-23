"""
    Given an array of integers and a positive integer k,
    get the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k
"""

def divisibleSumPairs(n, k, ar):
    total = 0

    for m in range(n):
        
        start = m
        while start + 1 < n:
            if (ar[m] + ar[start+1]) % k == 0:
                total += 1
            start += 1

    return total

assert divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]) == 3
assert divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5