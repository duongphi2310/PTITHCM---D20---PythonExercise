# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function is_anagrams to check whether two words are anagrams,
# the function returns True is two words are anagrams,
# otherwise, return False; then write a code to test the function.

# For example, 
# - Input: race care
# - Output: True

def is_anagrams(x, y):
    if (sorted(x) == sorted(y)):
        return True
    else:
        return False

x, y = input().split()
print(is_anagrams(x, y), end = '')