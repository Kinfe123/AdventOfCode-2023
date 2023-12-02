config = {
    "red":12,
    "green":13,
    "blue":14,
}
total_id= 0
res = 0

non_possible = []
with open('./input.txt') as f:
    for inp in f:
        splitted_semi = inp.split(':')
        game_id = splitted_semi[0].split(' ')[1]

        splitted_semi = splitted_semi[1:]
        splitted_semi = "".join(splitted_semi)
       
        total_id += int(game_id)
        splitted_semi = splitted_semi.split(';')
        temp =1
        map_ = {
            "red":1,
            "blue":1,
            "green":1,
            }   
        for i in range(len(splitted_semi)):
            
            possible = True
            
            curr_one = splitted_semi[i]
            
            comma_split = curr_one.split(',')
            
            
            for j in range(len(comma_split)):
                curr_cube = comma_split[j].split(' ')
                curr_color = curr_cube[-1]
                if '\n' in curr_color: curr_color = curr_color[:-1]
                map_[curr_color] = max(map_[curr_color] , int(curr_cube[1]))

        
        for keys , values in map_.items():
        
            temp*=values
        res+=temp

        
            
    


            
print('The result is: ' , res )
