

plants = []

with open('./test.txt') as f:
    for inp in f:
        plants.append(inp.replace('\n' , ''))

process = []
for i in plants:
    if i :
        process.append(i)


seeds = process[0]
process = process[1:]
t = seeds.split(':')[1][1:]

seeds = list(map(int , t.split(' ')))
min_ = float('inf')
print(seeds)
for each in process:
    nums = []
    for i in each.splitlines():
        if i[0].isdigit():
            temp = list(map(int , i.split()))
            nums.append(temp)
    print(nums)
    a  = []
    for s in range(len(seeds)):
        curr_seed = int(seeds[s])
        s = False
        for maps in nums:
            
            dist , source , p = maps
         
            if source <= curr_seed < source + p:
                r = curr_seed - source + dist
                a.append(r)
                min_ = min(min_ , r)
                s = True
                break
        
        else:
            a.append(curr_seed)
    seeds = a
    
    
       
print(seeds)

'''        
for i in range(len(seeds)):
    for each in process:
        print(each)
        s = False
        if each[0].isdigit():
            curr = list(map(int , each.split()))
            dist , source , p = curr
            if source <= int(seeds[i]) < source + p:
                r = int(seeds[i]) - source
                r  += dist
                a.append(r)
                min_ = min(min_ , r)
                s = True
                break

        if not s:
            a.append(int(seeds[i]))
        seeds = a
        print()
'''   
'''
for i in range(len(process)):
    curr = process[i]
    if curr[0].isdigit():
        process[i] = curr
    else:
        process[i] = ''
process = [i for i in process if i]
print('a' , process)
min_ = float('inf')
t = seeds.split(':')[1][1:]
a = []
seeds = list(map(int , t.split(' ')))
print(process)
for i in range(len(seeds)):
    s = False
    for j in range(len(process)):
        dist , source , p = process[j]
        if source <= int(seeds[i]) < source + p:
            r = int(seeds[i]) - source
            r  += dist
            a.append(r)
            min_ = min(min_ , r)
            s = True
            break

    if not s:
        a.append(int(seeds[i]))
    print(a , 'a')
    seeds = a

print(seeds)

'''
print(min_)


        
