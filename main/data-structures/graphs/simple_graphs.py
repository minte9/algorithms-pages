# SIMPLE GRAPHS
# -------------
# Concept:
#   - A graph is a data structure used to represent relationships.
#   - It is made of: vertices (nodes) and edges (relationships).
#
# Unline stacks of queue: 
#   - There is NO top or front
#   - connections can be many-to-many
#
# Real-life graphs: 
#   - social networks
#   - flight routes
#   - recommendations systems
# 
# Exampl: Friend relationships
#   - We use a dictionary
#   - Each key is a vertex
#   - Each list contains connected vertices
#   - Connections are biderectional
# -----------------------------------------

friends = {
    'Alice': ['Bob', 'Diana', 'Fred'],
    'Bob': ['Alice', 'Cynthia', 'Diana'],
    'Cynthia': ['Bob'],
    'Diana': ['Alice', 'Bob', 'Fred'],
    'Elise': ['Fred'],
    'Fred': ['Alice', 'Diana', 'Elise'],
}

print("Alice's friends:", friends['Alice'])
# -----------------------------------------
# Alice's friends: ['Bob', 'Diana', 'Fred']

