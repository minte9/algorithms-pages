""" Flood Fill
Begins on one pixel and spreads until it meets a non-white pixel, 
then it moves on to the neighbors and so on.
Arguments to pass are xy coordinates to user for the 4 neighbours 
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

def show_list(A):
    width = len(A[0])
    height = len(A) 

    for y in range(height):
        for x in range(width):
            print(A[y][x], end="")
        print('')
    print('')

def flood_fill(A, start):
    y, x = start
    A[y][x] = '0'

    top = y-1, x
    right = y, x+1
    bottom = y+1, x
    left = y, x-1

    # NORTH
    y, x = top
    if A[y][x] == ' ': 
        A[y][x] = '0'
        flood_fill(A, top) # Recursive

    # EAST
    y, x = right
    if A[y][x] == ' ': 
        A[y][x] = '0'
        flood_fill(A, right)

    # SOUTH
    y, x = bottom
    if A[y][x] == ' ': 
        A[y][x] = '0'
        flood_fill(A, bottom)

    # WEST
    y, x = left
    if A[y][x] == ' ': 
        A[y][x] = '0'
        flood_fill(A, left)

    return A # Base case

flood_fill(A, (1, 4))
show_list(A)

"""
    ||||||||||||||||||||||||||||||
    ||000000000000000000||     |||
    ||00000000|||||0000||     ||||
    ||||||0000||  ||000||   ||||||
    ||||00000||    ||000||     |||
    |||0000000||||||000000||   |||
    ||||||||000000000000||||||||||
    ||||||||||||||||||||||||||||||
"""