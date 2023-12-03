grid = set()
lists = []
with open('./input.txt' ) as f:
    for inp in f:
        lists.append(inp[:-1])
numbers = []

def inbound(x, y):
    return 0 <= x < len(lists) and 0 <= y < len(lists[0])
for r in range(len(lists)):
    s = ''
    start = [-1 , -1]
    for c in range(len(lists)):

        
        if lists[r][c].isdigit():
            
            
            s+=lists[r][c]
            if start[0] == -1 and start[1] ==-1:
                start[0] , start[1] = r , c
      
        else:
            
            if s:
                tr, tc = start
                poss = False
                for cr in [tr-1 , tr , tr+1]:
                    for cc in [tc-1 , tc, tc+1]:
                        if inbound(cr , cc) and lists[cr][cc] != '.' and not lists[cr][cc].isdigit():
                            #print('found : ', lists[cr][cc]  ,(cr , cc) , start)
                            poss = True
                            break
                    if poss:
                        break
                if poss:
                    if s not in numbers:
                        numbers.append(s)
                tr , tc = r , c
                poss = False
                for cr in [tr-1 , tr , tr+1]:
                    for cc in [tc-1 , tc, tc+1]:
                        if inbound(cr , cc) and lists[cr][cc] != '.' and not lists[cr][cc].isdigit():
                            #print('found : ', lists[cr][cc] , (cr , cc) , (r , c) )
                            poss = True
                            break
                    if poss:
                        break
                if poss:
                    if s not in numbers:
                        numbers.append(s)
                
                
            s = ''
            start = [-1 , -1]
print(numbers)
numbers = sum([int(i) for i in numbers])
print(numbers)
                
        
        
