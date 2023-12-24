import sys
from collections import *


grid = []

memo = defaultdict(tuple)

with open('./input.txt') as f:
    for inp in f:
        inp = inp.replace('\n' , '')
        grid.append([i for i in inp])

curr_st = 327
width = len(grid[0])
height = len(grid)
target_step = 26501365
dxn = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]

seen = set()
garden = defaultdict(set)
queue = []

for y in range(height):
    for x in range(width):
        if grid[y][x] == "S":
            curr = (x , y , 0)
            queue.append(curr)
            
while queue:
    x, y, step = queue.pop()

    if (x, y, step) in seen:
        continue

    seen.add((x, y, step))

    '''if (x , y , step) in memo:
        old_x , old_y = garden[step]
        garden[step] = (old_x * -1 * x, old_y )'''
        

    if grid[y % height][x % width] in ".S":
        if  not (step - 65) % 131:
            garden[step].add((x, y))
    else:
        continue

    if step == curr_st:
        continue

    for dx, dy in dxn:
        queue.append((x + dx, y + dy, step + 1))

steps = 327
score = len(garden[steps])
increment = len(garden[steps]) - len(garden[steps - width])
while steps != target_step and steps < target_step:
    increment += 30188
    
    score += increment

    steps += width

print('Waiting for you: ' , score)

