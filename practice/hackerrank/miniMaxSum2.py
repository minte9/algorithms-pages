def miniMaxSum(arr):
    total = 0    
    min_val = arr[0]
    max_val = arr[0]

    for n in arr:
        total += n
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
    
    print(min_val, max_val)

    min_sum = total - max_val
    max_sum = total - min_val
            
    print(f"{min_sum} {max_sum}")

miniMaxSum([1, 2, 3, 4, 5])