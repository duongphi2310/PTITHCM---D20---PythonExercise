# Edit distance is a string metric that quantifies
# how dissimilar two strings are to one another,
# that is measured by counting the minimum number of operations
# (delete, insert, replace) required to transform one string into the other. 

# Write a function compute_edit_distance to compute edit distance 
# between two strings and write a code to check your function.


# Test data 1
# Input: kitten, sitting
# Output: 3 

# Test data 2
# Input: bear, hear 
# Output: 1

s = input()
ss = s.split(", ")
s1 = ss[0]
s2 = ss[1]
if   len(s1) > len(s2):
    length = len(s1) - len(s2)
    for i in range(len(s2)):
        if (s1[i] != s2[i]):
            length = length + 1
elif len(s1) < len(s2):
    length = len(s2) - len(s1)
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            length = length + 1 
else:
    length = 0
print(length, end = '')