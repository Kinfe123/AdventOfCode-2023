from collections import defaultdict , Counter
grid = []
with open('./test.txt') as f:
    for inp in f:
        inp = inp.replace('\n' , '')
        grid.append([i for i in inp])

print(grid)



dxn = {
    ">": (0 , 1 ),
    '<': (0 , -1),
    "v": (1 , 0),
    '^': (-1 , 0)

}

path_track= []
paths = []
more_dxn = [(1 , 0), (-1 , 0) , (0 , 1) , (0, -1)] 
row  , col = len(grid) , len(grid[0])
def inbound(x , y):
    return 0 <= x < row and 0 <= y < col
def explore(x , y , visited , count ):
    print('Hello world' , count ,x,y)
    if x == row - 1:
        paths.append(count)
    if inbound(x , y) and (i , j) not in visited:
        path_track.append((x , y))
        curr = grid[x][y]
        visited.add((x , y))
        if curr  != '.' and curr in dxn:
            dx , dy  = dxn[curr]
            
            new_x , new_y =  x + dx , y + dy
            visited.add((new_x , new_y))

            explore(new_x , new_y , visited , count + 1)

        elif curr == '#':
            return 
        else:
            for cx , cy in more_dxn:
                new_x , new_y = x+cx , y+cy
                if grid[new_x][new_y] == '.':
                    visited.add((new_x , new_y))
                    explore(new_x , new_y , visited ,  count + 1)
                elif grid[new_x][new_y] in dxn:
                    dx , dy = dxn[grid[new_x][new_y]]
                    
                    visited.add((new_x + dx , new_y+ dy))
                    explore(new_x + dx , new_y + dy, visited  , count + 1)
                    


        
            
        
        


visited = set()

print('The row: ' , row , ' and col: ' , col, path_track)
    
for i in range(row):
    for j in range(col):
        if grid[i][j] == '.' and (i  , j) not in visited:
            
            explore(i , j , visited , 0)


print(paths)
