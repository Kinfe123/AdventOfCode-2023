res = 0
max_tst , max_p = 6, 190

with open('./input.txt') as f:
    ans = [1]*max_p
    for inp in f:
        inp = inp.replace('\n', '')
        semi = inp.split(':')
        
        cards = semi[1]
        piped = cards.split('|')
        card_num = int(semi[0].split()[1])
        
        
        sample  , winning = piped[0] , piped[1]
       
        sample , winning = list(map(str , sample.split())) , list(map(str , winning.split() ))
        
        set_winning = set(winning)
        score = 0
        
        for i in sample:
            if i in set_winning:
                score+=1
       
        if score:
            for i in range(card_num+1-1 , card_num+score+1-1):
                ans[i] += ans[card_num-1]
        
            
            
            
        
        
    print(sum(ans))
