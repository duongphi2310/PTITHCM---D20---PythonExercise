# Write a function is_unique that takes a list 
# and prints True if there is any element that appears more than once,
# otherwise, prints False; then write a code to check the function.

# For example, 
# Input: 1, 2, 3, 4, 3
# Output: True

def is_unique(s):
    sset = set()
    for i in s:
        if i in sset:
            return True
        else:
            sset.add(i)
    return False

s = list(map(int, input().split(', ')))
#s_sort = (sorted(s))
print(is_unique(s), end = '')