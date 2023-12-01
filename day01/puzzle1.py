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
    
        d = [c for c in inp if c.isdigit()]
        

        
        summed += int(d[0] + d[-1])
print(summed)        
        
    
