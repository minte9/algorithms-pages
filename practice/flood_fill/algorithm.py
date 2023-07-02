""" Flood Fill
Begins on one pixel and spreads until it meets a non-white pixel.
Then it moves on to the neighbors and so on.

Base case: xy coordinates on the edge of the image or if not the old color
Arguments to pass: xy coordinates to user for the 4 neighbours 
Arguments closer to base: algorithm runs out of pixels to check
"""
A = [
    list('||||||||||||||||||||||||||||||'),
    list('||                  ||     |||'),
    list('||        |||||    ||     ||||'),
    list('||||||    ||  ||   ||   ||||||'),
    list('||||     ||    ||   ||     |||'),
    list('|||       ||||||      ||   |||'),
    list('||||||||            ||||||||||'),
    list('||||||||||||||||||||||||||||||'),
]

# Width and height
w = len(A[0])
h = len(A) 

# Show image
def show(A):
    for y in range(h):
        for x in range(w):
            print(A[y][x], end="")
        print()
    print()

show(A)

# Flood Fill
def fill(A, start):
    y, x = start

    A[y][x] = '0'

    top = y-1, x
    right = y, x+1
    bottom = y+1, x
    left = y, x-1

    # Check north
    y, x = top
    if A[y][x] == ' ': A[y][x] = '0'; fill(A, top) # Recursive

    # Check east
    y, x = right
    if A[y][x] == ' ': A[y][x] = '0'; fill(A, right)

    # Check south
    y, x = bottom
    if A[y][x] == ' ': A[y][x] = '0'; fill(A, bottom)

    # Check east
    y, x = left
    if A[y][x] == ' ': A[y][x] = '0'; fill(A, left)

    return A # Base case

# Copy of A (to be used in first fill)
B = A[:]

# Start fill
fill(B, (1, 4))

# Show final result
show(B)

"""
    ||||||||||||||||||||||||||||||
    ||                  ||     |||
    ||        |||||    ||     ||||
    ||||||    ||  ||   ||   ||||||
    ||||     ||    ||   ||     |||
    |||       ||||||      ||   |||
    ||||||||            ||||||||||
    ||||||||||||||||||||||||||||||

    ||||||||||||||||||||||||||||||
    ||000000000000000000||     |||
    ||00000000|||||0000||     ||||
    ||||||0000||  ||000||   ||||||
    ||||00000||    ||000||     |||
    |||0000000||||||000000||   |||
    ||||||||000000000000||||||||||
    ||||||||||||||||||||||||||||||
"""