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
        for i in range(len(splitted_semi)):
            possible = True
            
            curr_one = splitted_semi[i]
            
            comma_split = curr_one.split(',')
          
            for j in range(len(comma_split)):
            
                curr_cube = comma_split[j].split(' ')
            
                curr_color = curr_cube[-1]
                if "\n" in curr_color: curr_color = curr_color[:-1]
               
                if config[curr_color] < int(curr_cube[1]):
                    
                    non_possible.append(int(game_id))
                    possible = False
                    break
print(total_id , non_possible)
print(total_id - sum(list(set(non_possible))))
