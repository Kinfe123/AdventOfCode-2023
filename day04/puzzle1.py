from collections import defaultdict

res = 0
ans = defaultdict(int)
max_tst, max_puzzle = 6 , 190
r = [1] * max_tst

with open('./test.txt') as f:
    for inp in f:
        inp = inp.replace('\n', '')
        semi = inp.split(':')
        cards = semi[1]
        piped = cards.split('|')
        
        sample  , winning = piped[0] , piped[1]
       
        sample , winning = list(map(str , sample.split())) , list(map(str , winning.split() ))
        print(sample , winning)
        set_winning = set(winning)
        score = 0
        for i in sample:
            if i in set_winning:
                score+=1
       
        if score:
            for i in range(1 , score+1):
                r[card_num + i] += r[i]
                
            
        
print(sum(r))
