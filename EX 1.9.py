# Write a program that gets a list L and print the most Frequently Occurring Items in L.
# For example, 
# Input: 1, 2, 3, 3, 0, 1
# Output: 1, 3

from collections import Counter

s = input().split(", ")
dem = Counter(s);
m = max(dem.values())
r = []
for i in dem:
    if dem[i] == m:
        r.append(i)
check = True
for i in range(0, len(r)):
    if (check):
        print(r[i], end = '')
        check = False
    else:
        print(",", r[i], end = '')