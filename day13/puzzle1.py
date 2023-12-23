res = 0
grid = []

def generate(grid):
    R = len(grid)
    C = len(grid[0])
            
    ans = 0
    part2 = True
    for c in range(C-1):
        test = 0
        for dc in range(C):
            left = c-dc
            right = c+1+dc
            if 0<=left and left < right and  right<C:
                for r in range(R):
                    if grid[r][left] != grid[r][right]:
                                
                        test += 1
        if test == (1 if part2 else 0):
            ans += c+1
    for r in range(R-1): 
        test = 0
        for dr in range(R):  
            up = r-dr
            down = r+1+dr
            if 0<=up and up < down and down<R:
                for c in range(C):
                    if grid[up][c] != grid[down][c]:
                        test +=1
        if test ==(1 if part2 else 0):
            ans += 100*(r+1)



            
    return ans




    
with open('./input.txt') as f:
    for inp in f:
        inp = inp.replace('\n' , '')
        if inp:
            grid.append([i for i in inp])
        else:
            res += generate(grid)
            grid = []
if grid:
    res+=generate(grid)

print(res)
