""" Find the mininum number of coins to make the change for 336.
    Denominators list is [1, 2, 3, 5, 10, 20, 30, 50, 100, 150].
    Duplicates are allowed but only for small coins, less than 100.
"""

def coin_change(target):
    denominators = [1, 2, 3, 5, 10, 20, 30, 50, 100, 150]
    result = []

    for v in reversed(denominators):

        if (v < 100):
            while v <= target - sum(result):
                result.append(v)
        else:
            if v <= target - sum(result):
                result.append(v)
    return result


target = 369
change_list = coin_change(target)

assert target == sum(change_list)
print(change_list)