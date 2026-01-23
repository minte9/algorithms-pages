# HASH TABLE - O(1)
# -----------------
# Example:
#   - Simple thesaurus application to exemplify hash table storing data process.
#   - The user searches for an word and the application returns one synonim (O(1)).
#
# Implementation:
#   - We implement a tiny custom "hash table" for strings made of letters a-e.
#   - It does not handle many real-world edge cases.
#   - This version is simplified for teaching
#
# Mapping:
#   - A tiny character-to-number map used by our hash function.
#   - Only lowercase letters are supported in this example.
# -------------

class HashTable:
    
    def __init__(self):
        self.capacity = 16
        self.table = [None] * self.capacity
        self.size = 0

    def _hash(self, x: str) -> int:  # List key is int
        h = 0
        base = 257
        for ch in x:
            h = (h * base + ord(ch)) % self.capacity
        return h

    def __setitem__(self, key, val):
        idx = self._hash(key)
        self.table[idx] = val  # Average O(1)
        self.size += 1

    def __getitem__(self, key):
        idx = self._hash(key)
        return self.table[idx]  # Average O(1)

thesaurus = HashTable()

# Insert
thesaurus['bad'] = 'evil'
thesaurus['cab'] = 'taxi'

# Search
print(thesaurus['bad'])  # evil
print(thesaurus['cab'])  # taxi

# Update
thesaurus['cab'] = 'taxiii'
print(thesaurus['cab'])  # taxiii
