# Write a function rotate(k, tmp_list) to cyclically rotate a given array clockwise by k.
# Test data 1
# Input 1:
#     1 3 2 5 7
# Output 1: 
#     7 1 3 2 5

# Test data 2
# Input 3:
#     1 3 2 5 7
# Output 3: 
#     2 5 7 1 3

def rotate(k, tmp_list):
    x = tmp_list[-k:] + tmp_list[:-k]
    for i in range(0, len(x)):
        print(x[i] + " ", end = "")

k = int(input())
tmp_list = input().split(" ")
rotate(k, l)