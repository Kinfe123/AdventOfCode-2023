from collections import Counter, defaultdict , deque

mapper = defaultdict(list)

sq = ''
process = []
with open('./input.txt') as f:
    for inp in f:
        if inp and inp != '\n':
            process.append(inp.replace('\n'  , ''))

    


sq = process[0]
process = process[1:]
for i in range(len(process)):
    curr = process[i]
    curr = curr.split('=')
    mapper[curr[0].replace(' ', '')] = curr[1][2:-1].replace(' ' , '').split(',')

start_node = 'AAA'
path = 0
q = deque(sq)

r = 0
while start_node != 'ZZZ':
        
        dxn = sq[r] 
        temp = 0
      
        if dxn == 'R':
            temp = 1
                  
        start_node = mapper[start_node][temp]
        r+=1
        r%=len(sq)
        path += 1
print(path)
            
    
