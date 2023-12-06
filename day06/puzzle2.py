

d , t = [] , []
keys= []
data = ''
with open('./input.txt') as f:
    data = f.read()

for i in data.splitlines():
    cur = i.split(':')[1]
    cur = cur.strip()
    cur = list(map(int  , cur.split()))
    cur = [str(i) for i in cur]
    cur = ''.join(cur)
    
    d.append(cur)
dd = int(d[0])
t = int(d[1])
keys.append((dd , t))
print(keys)
collect = []
for i in range(len(keys)):
    curr = keys[i]
    tt = curr[0]
    temp = []
    for i in range(tt):
        cal = (i * (tt - i))
        if cal > curr[1]:
            temp.append(i)
    collect.append(temp)

        
res = 1
for i in range(len(collect)):
    res *= len(collect[i])
print(res)

