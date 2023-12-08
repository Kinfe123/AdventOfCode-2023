from collections import Counter, defaultdict , deque
from math import lcm
mapper = defaultdict(list)

sq = ''
process = []
with open('./input.txt') as f:
    for inp in f:
        if inp and inp != '\n':
            process.append(inp.replace('\n'  , ''))

    


sq = process[0]
collect = []
process = process[1:]
for i in range(len(process)):
    curr = process[i]
    curr = curr.split('=')
    src = curr[0].replace(' ', '')
    mapper[src] = curr[1][2:-1].replace(' ' , '').split(',')
    if src[2] == "A":
        collect.append(src)
start_node = 'AAA'
l= []
for each in collect:
    start_node = each
    r , path = 0 , 0
    while start_node[2] != 'Z':
        
        dxn = sq[r] 
        temp = 0
      
        if dxn == 'R':
            temp = 1
                  
        start_node = mapper[start_node][temp]
        r+=1
        r%=len(sq)
        path += 1
    l.append(path)

print(lcm(*l))
            
    
