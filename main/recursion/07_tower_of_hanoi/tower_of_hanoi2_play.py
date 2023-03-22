""" Tower of Hanoi Interactive
"""
import sys

N = 3
towers = {
    'A': list(reversed(range(1, N + 1))),
    'B': [],
    'C': []}

def move(start, end):
    disk = towers[start].pop()
    towers[end].append(disk)

def show_board():
    rows = []
    for key, values in towers.items():
        rows.append('[' + ''.join(str(v) for v in values) + ']')
    print('\t'.join(rows))

def play():
    while True:

        show_board()
        m = input(":").upper()
        
        if m == 'Q':
            sys.exit()
        
        start, end = m[0], m[1]
        
        if len(towers[start]) == 0:
            print('Illegal move')
            continue
        if len(towers[end]) > 0:
            if towers[start][-1] > towers[end][-1]: 
                print('Illegal move')
                continue
        if start not in 'ABC' or end not in 'ABC' or start == end: 
            print('Illegal move')
            continue

        move(start, end)

        if towers['B'] == list(reversed(range(1, N + 1))):
            show_board()
            print('Solved!')
            sys.exit()


print("--------------")
print('Tower of Hanoi')
print('Type two letter from abc (start and end tower), type Q to quit ...')
print("--------------")

play()