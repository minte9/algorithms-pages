""" Coin change

Problem: Using a set of coins, 
find the mininum number of coins to make the change.

Algorithm: Start with the largest denominator that is less than or equal 
with the target ammount and continue with the smaller ones.
"""

D = [1, 5, 10, 25]
R = []

target = 63

for n in reversed(D):
    while n <= target - sum(R):
        R.append(n)

print(R, f"Mininum number of coins = {len(R)}")

"""
    [25, 25, 10, 1, 1, 1] Mininum number of coins = 6
"""