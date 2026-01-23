# HASHING - BASICS
# ----------------
# Concept:
#   - Hashing is the process of taking characters and converting them to number.
#
# Note:
#   - Real hash functions are one-way and produce fixed-size outputs.
#   - These examples are simplified for learning.
# -------------------------------------------------------

mapping_example = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 1) Hashing encoding
# -------------------
def hashing_encoding(x: str) -> str:
    res = ""
    for char in x:
        res += str(mapping_example[char])
    return res

hash = hashing_encoding('BAD')
print(hash)  
# ---------------------------
# 214


# 2) Hashing additive
# -------------------
def hasing_sum(x: str) -> str:
    res = 0
    for char in x:
        res += mapping_example[char]
    return res

hash = hashing_encoding('BAD')
print(hash)
# ----------------------
# 7
