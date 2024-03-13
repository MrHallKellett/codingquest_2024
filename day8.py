from collections import defaultdict
from math import inf as INF
from itertools import combinations
with open("day8.txt") as f:
    ACTUAL_DATA = f.read().splitlines()

EXPECTED = 13

def find_combinations(options, target, path="", combinations=0, cache=None):

    
    
    result = 0 if not path else eval(path)


    if target - result in cache:
        return combinations + cache[target - result]
    elif result == target:
        return combinations + 1
    elif result < target:
        for option in options:
            combinations = find_combinations(options, target, path+option, combinations, cache)
            

    return combinations

    

    
        

def solve(options, target):
    cache = {}
    options = [f"+{o}" for o in options]
    for sub_target in range(1, target+1):
        cache[sub_target] = find_combinations(options, sub_target, cache=cache)
        

    
    return cache[target]
                

 
if __name__ == "__main__":
    target = 5
    options = [1, 2, 3]
    assert solve(options, target) == EXPECTED
    
    target = 856
    options = [40, 12, 2, 1]
    
    print("TEST PASSED!!!")

    
    print(solve(options, target))


