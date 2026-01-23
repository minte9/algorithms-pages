"""
    A girl want to share a chocolate bar with a boy.
    Chocolate's sqares has an integer on it.

    The girl to share a contiguous segment so that:
        - the length of the segment maches the boy's birth month
        - the sum of square's numbers is equal to boy's birth day

    Sample:
        s = [2, 2, 1, 3]
        d, m = 4, 2
    Output:
        2 segments / [2, 2] and [1, 3]
"""

def birthday(s, d, m):

    total = 0
    for i in range(len(s)):

        segment = 0
        for j in range(m):
            if (i + j) < len(s):
                segment += s[i + j]

        if segment == d:
            total += 1

    return total


assert birthday([1, 2, 1, 3, 2], 3, 2) == 2
assert birthday([2, 2, 1, 3], 4, 2) == 2
assert birthday([1, 1, 1, 1, 1, 1], 3, 2) == 0
assert birthday([4], 4, 1) == 1
