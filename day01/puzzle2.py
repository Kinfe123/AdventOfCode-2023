import re
number = 2237
lists = []
max_ = float('-inf')
summed = 0
numbers = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine' ]
digit_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
max_input = 1000


with open('./input.txt', 'r') as f:
    for inp in f:
        print('THe current line: ' , inp)
        temp = ''
        res = []
        possible =[]
        for i in numbers:
            if i in inp:
                possible.append([inp.index(i) , i])

        first_  , last_ = [ ] , []
        possible.sort(key=lambda x: x[0])
        if possible:
            first_  , last_ = possible[0] , possible[-1]
            temp = digit_mapping[first_[1]] + digit_mapping[last_[1]]
        for i in range(len(inp)):
            curr = inp[i]
            if curr.isdigit():
                if first_:
                    indx , val = first_
                    if indx < i:
                        temp = digit_mapping[val]
                    else:
                        temp = str(curr)
                else:
                    temp = str(curr)
                break
        for i in range(len(inp)-1 , -1 , -1):
            curr = inp[i]
            if curr.isdigit():
               
                if last_:
                    indx , val = last_
                    if indx > i:
                        temp += digit_mapping[val]
                    else:
                        temp+= str(curr)
                else:
                    temp += str(curr)
                break

        
        summed += int(temp)

        
        
       
            
    

    
    
    
        
        
    

       

    
        


print(summed)
        
        
    
