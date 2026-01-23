"""
    Given an array of integers, calculate and print the ratio of elements that are 
    positive, negative and zero. Print the numbers with exact 6 decimal numbers. 
"""

def pluMinus(arr):

    size = len(arr)
    
    res = [0.000000, 0.000000, 0.000000]
    for n in arr:
        if n > 0:
            res[0] += 1/size
        elif n < 0:
            res[1] += 1/size
        else:
            res[2] += 1/size

    return res

res = pluMinus([1, 1, 0, -1, -1])

for x in res:
    print(f"{x:.6f}")