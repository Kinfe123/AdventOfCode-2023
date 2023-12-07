from collections import Counter , defaultdict
mapper = defaultdict(int)
process = []

with open('./input.txt') as f:
    for inp in f:
        curr = inp.replace('\n','').split(' ')
        process.append([curr[0] , curr[1]])
process.sort(key= lambda x: len(set(x[0])))
def get_score(item):
    hand, bid = item

    counts = sorted(list(Counter(hand.replace("J", "")).values()))

    if len(counts) > 0:
        counts[-1] += hand.count("J")
    else:
        counts.append(5)
    if 5 in counts:
        type = 6
    elif 4 in counts:
        type = 5
    elif 3 in counts:
        if 2 in counts:
            type = 4
        else:
            type = 3
        
    elif 2 in counts:
        if counts.count(2) == 2:
            type = 2
        else:
            type = 1
        
    else:
        type = 0

    values = list(map("J23456789TJQKA".index, hand))

    return (type, values)

process.sort(key=get_score)
result =0
for i in range(len(process)):
    curr = int(process[i][1])
    result+= (i + 1) * curr
print(result)
