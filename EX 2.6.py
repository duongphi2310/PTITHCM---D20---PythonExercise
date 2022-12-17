# Write a function get_k_common_numbers to find
# the occurrences of top k most common numbers in a given list.

# If there are numbers that have the same occurrences
# and the most common numbers are larger than k, then the smaller number is chosen. 

# Please don't use Counter of collections library.
# Write a program to test your function.

# Test data 1:
# Input:
#     3  // as k
#     10, 90, 70, 80, 50, 10, 70, 90, 90  // as a list
# Output:
#     (90, 10, 70) // as k most common numbers
#     (3, 2, 2) // as corresponding occurrences of k most common numbers

# Test data 2:
# Input:
#     2
#     10, 90, 70, 80, 50, 10, 70, 90, 90
# Output:
#     (90, 10), (3, 2)

def get_k_common_numbers(k, numbers):
    xuathien = {}
    for number in numbers:
        if number in xuathien:
            xuathien[number] = xuathien[number] + 1
        else:
            xuathien[number] = 1
    sortxuathien = sorted(xuathien.items(), key=lambda item: item[1], reverse=True)
    
    common_numbers = []
    common_occurrences = []
    for i in range(min(k, len(sortxuathien))):
        common_numbers.append(int(sortxuathien[i][0]))
        common_occurrences.append(int(sortxuathien[i][1]))
    
    return tuple(common_numbers), tuple(common_occurrences)

k = int(input())
numbers = input().split(", ")
common_numbers, common_occurrences = get_k_common_numbers(k, numbers)
print(common_numbers,",",common_occurrences)