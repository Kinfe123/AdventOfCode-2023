grid = []

with open('./input.txt') as f:
    for inp in f:
        grid.append(inp.replace('\n' , ''))
print(grid)

galaxies = []

expand_row , expand_col = [] , []
expand_row = [all([grid[i][j] == "." for j in range(len(grid[0]))]) for i in range(len(grid))]
expand_col = [all([grid[i][j] == "." for i in range(len(grid))]) for j in range(len(grid[0]))]
factor = 10 ** 6
def calc(x , y):
    first_a , first_b = x
    sec_a , sec_b = y

    res = 0
    for i in range(min(first_a , sec_a) , max(first_a , sec_a)):
        res += 1
        if expand_row[i]:
            steps = (factor - 1)
            res += steps
    for i in range(min(first_b , sec_b), max(first_b , sec_b)):
        res += 1
        if expand_col[i]:
            steps = (factor - 1)
            res += steps
            
    return res
        
for i in range(len(grid)):
    '''if all(c == '.' for c in grid[i]):
        
        expand_row.append(True)
    else:
        expand_row.append(False)'''
    for j in range(len(grid[0])):
        '''if len(expand_col) <= len(grid[0]):
            if all(c == '.' for c in grid[j]):
                expand_col.append(True)
            else:
                expand_col.append(False)
        '''
        if grid[i][j] == '#':
            galaxies.append((i , j))
total = 0
for i in range(len(galaxies)):
    for j in range(i+1 , len(galaxies)):
        total  += calc(galaxies[i] , galaxies[j])

print(total)
        
