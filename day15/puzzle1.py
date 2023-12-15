lists = []

with open('./input.txt') as f:
    lists = list(map(str , f.read().replace('\n' , '').split(',')))
    

res = 0
def hash(curr):
    summ = 0
    for i in curr:
        summ += ord(i)
        summ *= 17
        summ %= 256
    return summ
for i in range(len(lists)):
    curr = lists[i]
    res += hash(curr)

print(res)
