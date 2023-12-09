lists = []
with open('./input.txt') as f:
    for inp in f:
        lists.append(list(map(int , inp.replace('\n' , '').split(' '))))
def process(li):
    temp = []
    for i in range(len(li) - 1):
        diff = li[i+1] - li[i]
        temp.append(diff)
        
        if sum(temp) != 0:
            return li[-1] + process(temp)
        else:
            temp.append(diff)
            return li[-1]
        

res = 0

def p(li):
 
    res = 0
    temp = li
    pp =[]
    while all(x == 0 for x in li):
        pp.append(li[0])
       
        temp = []
        for i in range(len(li)-1):
            diff = li[i+1]-li[i]
            temp.append(diff)
        li = temp
    return pp


def final(x):
    if all(i == 0 for i in x):
        return 0
    else:
        seq = [(b - a) for a , b in zip(x , x[1:])]
        res = final(seq)
        return x[0] - res
ans = 0
for i in range(len(lists)):
    curr = lists[i]
    
    res = final(curr)
    ans += res
print(ans)
    
