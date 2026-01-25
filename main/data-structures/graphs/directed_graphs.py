# DIRECTED GRAPHS
# ---------------
# Relationships are not always mutual.
# In directed graphs connection is one-way.
#
# Example: Social medial follows:
#   - Alice follows Bob
#   - Bob does not have to follow Alice
# -------------------------------------

followees = {
    'Alice': ['Bob', 'Diana'],
    'Bob': ['Cynthia'],
    'Cynthia': ['Bob'],
}

assert 'Bob' in followees['Alice']
assert 'Alice' not in followees['Bob']

print("Bob is following Alice")
print("Alice is not following Bob")
# ---------------------------------
# Bob is following Alice
# Alice is not following Bob
