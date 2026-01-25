# OBJECT ORIENTED GRAPHS
# ----------------------
# Dictionary are great for simple graphs.
#
# Sometimes we need objects that provide us:
#   - behavior
#   - encapsulation
#   - clear relationships
#
# Example: 
#   - Friend relationships (mutual)
# ---------------------------------

class Vertex:
    def __init__(self, name):
        self.value = name
        self.adjacent_vertices = []  # LIST

    def add_adjacent(self, vertex):
        # Add connection
        self.adjacent_vertices.append(vertex)

        # Ensure mutual relationship
        if self not in vertex.adjacent_vertices:
            vertex.adjacent_vertices.append(self)

a = Vertex("Alice")
b = Vertex("Bob")
c = Vertex("Cynthia")

a.add_adjacent(b)
a.add_adjacent(c)
b.add_adjacent(c)

print("A neighbours:", [v.value for v in a.adjacent_vertices])
print("B neighbours:", [v.value for v in b.adjacent_vertices])

# ----------------------------------
# A neighbours: ['Bob', 'Cynthia']
# B neighbours: ['Alice', 'Cynthia']