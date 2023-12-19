from collections import defaultdict
memo = defaultdict(tuple)

def solve(config, nums):
    if config == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in config else 1

    if (config , nums) in memo:
        return memo[(config , nums)]
    result = 0
    
    if config[0] in ".?":
        result += solve(config[1:], nums)
        
    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            result += solve(config[nums[0] + 1:], nums[1:])


    memo[(config , nums)] = result 
    return result

res = 0


with open('./input.txt') as f:
    for inp in f:
        # do the stuff here

        curr_inp = inp.replace('\n' , '')
        config , seq = curr_inp.split(' ')
        seq = tuple(map(int , seq.split(',')))
        config = "?".join([config]*5)
        seq*=5
        res+=solve(config , seq)
print(res)


