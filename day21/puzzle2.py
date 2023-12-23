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

    

    if grid[y % height][x % width] in ".S":
        if (step - 65) % 131 == 0:
            garden[step].add((x, y))
    else:
        continue

    if step == 327:
        continue

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        queue.append((x + dx, y + dy, step + 1))

steps = 327
score = len(garden[steps])
increment = len(garden[steps]) - len(garden[steps - width])

while steps != 26501365:
    increment += 30188
    score += increment
    steps += width

print(score)

print(len(garden[64]))

