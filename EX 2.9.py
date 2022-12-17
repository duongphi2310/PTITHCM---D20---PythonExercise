# Write a function count_words that reads a string
# and return a list of only the words
# with more than k characters (not counting whitespace).

# Write a code to check your function.

# Test data 1
# Input: 
#     8
#     which is a perfectly legitimate word, so stop looking at me like that.
# Output:
#     [perfectly, legitimate]
def count_words(k, s):
    s2 = []
    for i in s:
        i = i.replace(",", "")
        i = i.replace(".", "")
        s2.append(i)
    check = True
    print("[", end = '')
    for i in range (0, len(s2)):
        ss = str(s2[i])
        if (len(ss) > k):
            if (check):
                print(s2[i], end = "")
                check = False
            else:
                print(",", s2[i], end = '')
    print("]", end = '')
    
k = int(input())
s = input().split(" ")
count_words(k, s)
