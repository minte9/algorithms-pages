# HASH TABLE - DICTIONARY
# -----------------------
# Buitl-in:
#   - In Python, dict() is a highly optimized hash table.
#   - In Java, we have HashMap 
#
# Fast lookps:
#   - O(1) on average
#
# Concept:
#   - An unordered array search is O(n)
#   - An ordered array binary search is O(log n)
#   - A hash table is O(1) average-case for get, set, delete


# 1) Using literal syntax {}
# --------------------------
prices = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.80,
}

# Searching
item = prices['banana']  # O(1)

# Inserting
prices["kiwi"] = 0.90  # O(1)

# Deleting 
del prices["banana"]  # O(1)

print(prices)
# -----------------------------------------
# {'apple': 0.5, 'orange': 0.8, 'kiwi': 0.9}


# 2) Using dict()
# ---------------
prices = dict([
    ("apple", 0.50),
    ("banana", 0.30),
    ("orange", 0.80),
])
print(prices)
# ------------------------------------------
# {'banana': 0.3, 'orange': 0.8, 'kiwi': 0.9}


# 3) Using zip()
# --------------
keys = ["apple", "banana", "kiwi"]
values = [0.50, 0.30, 0.90]

prices = dict(zip(keys, values))
print(prices)
# ------------------------------------------
# {'apple': 0.5, 'banana': 0.3, 'kiwi': 0.9}


