"""
Given five positive integers, find the minimum and maximum values that can be calculated 
by summing exactly four of the five integers. Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.
"""

def miniMaxSum(arr):
    # Write your code here
    
    max = 0
    min = sum(arr)
    
    for i in range(len(arr)):
        tmp = arr.copy()
        tmp[i] = 0 # remove one item
        
        if sum(tmp) > max:
            max = sum(tmp)
            
        if sum(tmp) < min:
            min = sum(tmp)
            
    print(f"{min}  {max}")


miniMaxSum([1, 2, 3, 4, 5])