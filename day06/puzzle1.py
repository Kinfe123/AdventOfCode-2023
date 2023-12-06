

d , t = [] , []
keys= []
data = ''
with open('./input.txt') as f:
    data = f.read()

for i in data.splitlines():
    cur = i.split(':')[1]
    cur = cur.strip()
    cur = list(map(int  , cur.split()))
    d.append(cur)
dd = d[0]
t = d[1]
for i in zip(dd , t):
    keys.append(i)

collect = []
for i in range(len(keys)):
    curr = keys[i]
    tt = curr[0]
    temp = []
    for i in range(0 , tt):
        cal = (i * (tt - i))
        if cal > curr[1]:
            temp.append(i)
    collect.append(temp)

        
res = 1
for i in range(len(collect)):
    res *= len(collect[i])
print(res)
