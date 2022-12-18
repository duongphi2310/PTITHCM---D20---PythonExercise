# Write a function called has_no_charx that returns True
# if the given word doesn’t have the letter x in it,
# otherwise, return False.
# Write a code to check your function.

# Test data 1
# Input: 
#     e
#     hello
# Output: 
#     False

# Test data 2
# Input: 
#     a
#     school
# Output: 
#     True

def has_no_charx(x, y):
    l = []
    for i in y:
        l.append(i)
    for i in x:
        if i in l:
            return False
        else:
            return True

x = input()
y = input()
print(has_no_charx(x, y), end = '')