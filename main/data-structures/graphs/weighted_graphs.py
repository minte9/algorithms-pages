# WEIGHTED GRAPHS
#----------------
# Concept:
#   - In some graphs, connections have values:
#     (distance, cost, time, price)
#
# Example:
#   - Flights between cities
#
# Vertices:
#   - Dallas -> Toronto costs $138
#   - Toronto -> Dalls costs $216
#
# Direction and cost both matters
# -------------------------------

class WeightedVertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}  # DICT

    def add_adjacent(self, vertex, price):
        self.adjacent_vertices[vertex.value] = price

d = WeightedVertex('Dallas')
t = WeightedVertex('Toronto')

d.add_adjacent(t, 138)
t.add_adjacent(d, 216)

print('Dallas flights:', d.adjacent_vertices)
print('Toronto flights:', t.adjacent_vertices)
# --------------------------------------------
# Dallas flights: {'Toronto': 138}
# Toronto flights: {'Dallas': 216}