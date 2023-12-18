import sys
grid = []

with open('./input.txt') as f:
    for inp in f:
        curr = inp.replace('\n' , 'n')
        grid.append([i for i in curr])


col = len(grid[0])
row = len(grid)

for _ in range(100):
    for y in range(row - 1, 0, -1):
        for x in range(col):
            if grid[y][x] == "O" and grid[y - 1][x] == ".":
                grid[y][x], grid[y - 1][x] = grid[y - 1][x], grid[y][x]

res = 0
for y in range(row):
    for x in range(col):
        if grid[y][x] == "O": res+= row-y
            

        




print(res)
