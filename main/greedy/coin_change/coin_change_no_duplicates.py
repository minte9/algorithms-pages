""" Coin change (variation)

No duplicates allowed in the result (set).
"""

COINS = [1, 2, 3, 5, 10, 20, 30, 50, 100, 130, 150]

def coin_change(target):
    R = set()
    remaining = target - sum(R)

    for n in reversed(COINS):
        if n <= remaining:
            R.add(n)
            remaining = target - sum(R)
    return R

assert sum(coin_change(326)) == 326

print(coin_change(326))

"""
    {1, 130, 5, 10, 150, 30}
"""