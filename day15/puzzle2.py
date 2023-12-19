lists = []
boxes = [[] for _ in range(256)]


with open('./input.txt') as f:
    curr = list(map(str , f.read().replace('\n' , '').split(',')))
    print('THe current step : ', curr)
    for step in curr:
        if "=" in step:
            label, length = step.split("=")
            length = int(length)

            v = 0
            for ch in label:
                v += ord(ch)
                v *= 17
                v %= 256

            for arr in boxes[v]:
                if arr[0] == label:
                    arr[1] = length
                    break
            else:
                boxes[v].append([label, length])
        elif step.endswith("-"):
            label = step[:-1]

            v = 0
            for ch in label:
                v += ord(ch)
                v *= 17
                v %= 256

            boxes[v] = [arr for arr in boxes[v] if arr[0] != label]
        
t = 0
for i, box in enumerate(boxes):
    for j, arr in enumerate(box):
        t += (i + 1) * (j + 1) * arr[1]

print(t)




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
