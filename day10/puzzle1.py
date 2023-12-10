from collections import deque

grid = []
r , c = -1  , -1
with open('./input.txt') as f:
    for inp in f:
      
        grid.append(inp.replace('\n', ''))


found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
    
        if grid[i][j] == 'S':
            
            r , c = i , j
            found = True
            break
    if found:
        break

visited = set()

que = deque()
que.append((r, c))
can_go_y = '|F7'
can_go_x = '-LF'
def inbound(x , y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) 

while que:
    cur_r , cur_c = que.popleft()
    cur_ch = grid[cur_r][cur_c]
    
    if  (cur_r , cur_c) not in visited and inbound(cur_r , cur_c):
       
        visited.add((cur_r , cur_c))
    
        if cur_ch in set(['|' , '7' , 'F' , 'S']) and inbound(cur_r + 1, cur_c) and  grid[cur_r+1][cur_c] in set(['|' , 'L' , 'J']):
            que.append((cur_r+1 , cur_c))
        if  cur_ch in set(['|' , 'L' , 'J' , 'S']) and inbound(cur_r -1 , cur_c) and grid[cur_r-1][cur_c] in set(['|' , '7' , 'F']):
            que.append((cur_r - 1, cur_c))
        if cur_ch in set(['-' , '7' , 'J' , 'S']) and inbound(cur_r , cur_c- 1 ) and grid[cur_r][cur_c-1] in set(['-' , 'F' , 'L']):
            que.append((cur_r , cur_c - 1))
        if cur_ch in set(['-' , 'F' , 'L' , 'S']) and inbound(cur_r , cur_c + 1) and  grid[cur_r][cur_c+1] in set(['-' , 'J' , '7']):
            que.append((cur_r , cur_c +1))
looped = len(visited)//2
print(looped)
    



