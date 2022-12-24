# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a code that takes two strings and prints True if they are anagrams and False otherwise.

# For example, 
# - Input: race care
# - Output: True

def check(x, y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False

x, y = input().split()
print(check(x, y))
