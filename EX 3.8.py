# Write a function find_combinations(n, k, tmp_list) to find all combination of n elements
# of a given array whose sum is equal to a given value k.

# Test data
# Input: 
#     4
#     53
#     [10, 20, 30, 40, 1, 2]

# Output: 
#     [10, 50, 1, 2]
#     [20, 30, 1, 2]

import ast
from itertools import combinations

def find_combinations(n, k, tmp_list):
    combs = []
    for comb in combinations(tmp_list, n):
        if sum(comb) == k:
            combs.append(list(comb))
    return combs

n = int(input())
k = int(input())
tmp_list_string = input()
tmp_list = ast.literal_eval(tmp_list_string)
a = find_combinations(n, k, tmp_list)
print("{}".format("\n".join(map(str, a))))