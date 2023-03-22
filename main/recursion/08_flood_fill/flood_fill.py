""" Flood Fill
Begins on one pixel and spreads until it meets a non-white pixel.
Then it moves on to the neighbors and so on.

Base case: xy coordinates on the edge of the image or if not the old color
Arguments to pass: xy coordinates to user for the 4 neighbours 
Arguments closer to base: algorithm runs out of pixels to check
"""
import copy

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

WIDTH, HEIGHT = len(A[0]), len(A)
print(WIDTH, 'x', HEIGHT)

def show(image):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(image[y][x], end='')
        print()
    print()

def floodFill(image, i, j):
    if image[i][j] != ' ': # Base case
        return

    image[i][j] = '0' # Change current

    neighbors = [
        (i, j + 1), # Up
        (i, j - 1), # Down
        (i - 1, j), # Left
        (i + 1, j), # Right
    ]
    for y, x in neighbors:
        if image[y][x] == ' ':
            if (x >= 0 and x < WIDTH) and (y >= 0 and y < HEIGHT):
                image = floodFill(image, y, x) # Recursive case
    
    return image

show(A)

B = copy.deepcopy(A)
C = copy.deepcopy(A)

floodFill(B, 1, 4)
floodFill(C, 1, 25)

show(B)
show(C)

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

    ||||||||||||||||||||||||||||||
    ||                  ||00000|||
    ||        |||||    ||00000||||
    ||||||    ||  ||   ||000||||||
    ||||     ||    ||   ||00000|||
    |||       ||||||      ||000|||
    ||||||||            ||||||||||
    ||||||||||||||||||||||||||||||
"""