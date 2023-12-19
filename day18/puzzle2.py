mapper = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

candy = [(0 , 0)]

bars = 0


mapper_dxn = ['R', 'D' , 'L' , 'U']
with open('./input.txt') as f:
    for inp in f:
        curr = inp.replace('\n' , '')
        dxn , num ,color  = curr.split()
        color_fmt = color[2:-1]
        for_dx , for_dy = mapper[mapper_dxn[int(color_fmt[-1])]]
        num = int(color_fmt[:-1] , 16)
        bars += num
        last_r , last_c = candy[-1]
        moved_x , moved_y = last_r + (int(num)*for_dx) , last_c + (int(num) * for_dy)
        candy.append((moved_x , moved_y))


print(candy)
#Shoelace implementation

area = 0
for i in range(len(candy)):
  
    a  ,  c = candy[i][0]  , candy[(i+1) % len(candy)][1]
    b = 0
    if i > 0:
        b = candy[i-1][1] 
    
    area += (a * (b - c))

area = abs(area)//2



interior_pt = area - bars // 2 + 1


print(interior_pt + bars)

