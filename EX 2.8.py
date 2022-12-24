# Edit distance is a string metric that quantifies
# how dissimilar two strings are to one another,
# that is measured by counting the minimum number of operations
# (delete, insert, replace) required to transform one string into the other. 

# Write a function compute_edit_distance to compute
# edit distance between two strings and write a code to check your function.

# Test data 1
# Input: kitten, sitting
# Output: 3 

# Test data 2
# Input: bear, hear 
# Output: 1

def compute_edit_distance(string1, string2):
  if not string1:
    return len(string2)
  if not string2:
    return len(string1)

  if string1[0] == string2[0]:
    return compute_edit_distance(string1[1:], string2[1:])
  
  return min(
    compute_edit_distance(string1[1:], string2) + 1,
    compute_edit_distance(string1, string2[1:]) + 1,
    compute_edit_distance(string1[1:], string2[1:]) + 1
  )
  
s = input().split(", ")
string1 = s[0]
string2 = s[1]
print(compute_edit_distance(string1, string2))