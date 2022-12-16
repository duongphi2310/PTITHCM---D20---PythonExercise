# Write a program to break an integer
# into a sequence of individual digits. 

# Test Data
# Input six non-negative digits: 123456
# Expected Output: 1 2 3 4 5 6

s = input()
for x in range(0, len(s)):
    if (x != len(s) - 1):
        print(s[x], end = ' ')
    else:
        print(s[x], end = '')
