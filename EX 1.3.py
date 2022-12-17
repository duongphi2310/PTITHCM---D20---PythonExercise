# A palindrome is a word that is spelled
# the same backward and forward,like "noon" and "redivider".
# Recursively, a word is a palindrome if the first and last
# letters are the same and the middle is a palindrome.
# Write a code to check if a string is a palindrome or not. 
# If a string S is a palindrome, print True, otherwise, print False.

def isPalindromes(s):
    return s == s[::-1]

s = input()
s = s.lower()
a = isPalindromes(s)
if a:
    print("True",  end = '')
else:
    print("False", end = '')