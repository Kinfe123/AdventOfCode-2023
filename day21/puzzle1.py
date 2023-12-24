import sys
from collections import *
grid = []
with open('./input.txt') as f:
    for inp in f:
        inp = inp.replace('\n' , '')
        grid.append([i for i in inp])
    


width = len(grid[0])
height = len(grid)

seen = set()
garden = defaultdict(set)
queue = []

for y in range(height):
    for x in range(width):
        if grid[y][x] == "S":
            queue.append((x, y, 0))

while len(queue) > 0:
    x, y, step = queue.pop()

    if (x, y, step) in seen:
        continue

    seen.add((x, y, step))

    if x < 0 or x >= width or y < 0 or y >= height:
        continue

    if grid[y][x] in ".S":
        garden[step].add((x, y))
    else:
        continue

    if step == 64:
        continue

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            queue.append((x + dx, y + dy, step + 1))

    

print(len(garden[64]))

