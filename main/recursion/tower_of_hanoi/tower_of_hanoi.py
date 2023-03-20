""" Tower of Hanoi
A puzzle with stacked disks, largest disk on the bottom.
The disks have a hole in center and can be moved on three poles.

To solve the puzzle, one player must move the disks 
from one pole to another.
The player can never place a larger disk on top of a smaller one.

Base case: move the smaller disk from start to end pole.
Recursive case for a tower with n disks:
solves n-1 case, move the nth disk, and then solves n-1 case again.

https://www.mathsisfun.com/games/towerofhanoi.html
"""

N = 3
towers = {
    'A': list(reversed(range(1, N + 1))),
    'B': [],
    'C': [],
}

def move(disk, start, end):
    towers[end].append(disk)

def topdisk(start):
    return towers[start].pop()

def solve(n, start, end, tmp):
    if n == 1:
        move(topdisk(start), start, end)    # Look Here
        show(n)
        return

    solve(n-1, start, tmp, end)             # Look Here
    move(topdisk(start), start, end)        # Look Here
    show(n)
    solve(n-1, tmp, end, start)             # Look Here
    return

def show(n):
    rows = []
    for key, values in towers.items():
        rows.append(''.join(str(v) for v in values))
    print(f'move {n} \t', '\t'.join(rows))

print('Start \t', ''.join(str(v) for v in towers['A']))
solve(N, 'A', 'B', 'C')

if towers['B'] == list(reversed(range(1, N + 1))):
    print('Solved!')

"""
    move     321
    move 1   32     1
    move 2   3      1       2
    move 1   3              21
    move 3          3       21
    move 1   1      3       2
    move 2   1      32
    move 1          321
"""