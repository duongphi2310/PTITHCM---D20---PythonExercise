# Write a function is_ascending that takes a list as a parameter
# and prints True if the list is sorted in ascending order
# and False otherwise. Then, write a code to check the function.
# Please do not sort the list, just check it.

# For example,
# Input: 1, 2, 3, 4
# Output: True

def is_ascending(s):
    if s == sorted(s):
        return True
    else:
        return False

s = input().split(", ")
print(is_ascending(s))