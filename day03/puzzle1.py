grid = set()
lists = []
with open('./test.txt' ) as f:
    for inp in f:
        lists.append(inp[:-1])
numbers = []


start_indx = set()
dxn = [[1 , 0] ,[0 , 1] , [1 , 1] , [-1, -1]]
res = 0
def inbound(x, y):
    return 0 <= x < len(lists) and 0 <= y < len(lists[0])
for r in range(len(lists)):
    s = ''
    start = []
    for c in range(len(lists)):
        s = set()
        curr = lists[r][c]
        if curr != '.' and not curr.isdigit() and curr == '*':
            for cr in range(r-1 , r+1+1):
                for cc in range(c-1  , c+1+1):
                    if inbound(cr, cc) and lists[cr][cc].isdigit():
                        while cc > 0 and lists[cr][cc-1].isdigit():
                            cc-=1
                        s.add((cr , cc))
                        start_indx.add((cr , cc))
            if len(s) == 2:
                pro = 1
                for each in s:
                    a , b = each
                    pro *= int(lists[a][b])
                res += pro

    
    
                    
print(res)               
                    

                
print(start_indx)

'''res = 0        
for start_x , start_y in start_indx:
    curr_num = ''
    while start_y < len(lists[0]) and lists[start_x][start_y].isdigit():
        curr_num += lists[start_x][start_y]
        start_y+=1
    res+=int(curr_num)
print(res)
'''
