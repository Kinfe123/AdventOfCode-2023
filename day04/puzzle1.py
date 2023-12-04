res = 0

with open('./test.txt') as f:
    for inp in f:
        inp = inp.replace('\n', '')
        semi = inp.split(':')
        cards = semi[1]
        piped = cards.split('|')
        sample  , winning = piped[0] , piped[1]
        print(sample , winning)
        sample , winning = list(map(str , sample.split())) , list(map(str , winning.split() ))
        print(sample , winning)
        set_winning = set(winning)
        score = 0
        for i in sample:
            
            if i in set_winning:
                score+=1
        print('score; ' , score)
        if score:
            res += 2 ** (score - 1)
        
print(res)
