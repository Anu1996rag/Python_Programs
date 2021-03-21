"""
converts the column name from the excel sheet into equivalent integer with A = 1

"""

import functools


def ss_decode_to_no(col):
    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


ss_decode_to_no("ZZ")

# brute force approach
result = 0
for i in "AZ":
    result *= 26
    result = result + (ord(i) - ord('A') + 1)
print(result)

# using lambda function
a = lambda result, c : result * 26 + ord(c) - ord('A') + 1
functools.reduce(a, "AZ", 0)

"""
converts the column name from the excel sheet into equivalent integer with A = 0

"""
# brute force approach
result = 0
for i in "AZ":
    result *= 26
    result = result + (ord(i) - ord('A'))
print(result)

# using lambda function
a = lambda result, c : result * 26 + ord(c) - ord('A')+1
print(functools.reduce(a, "AAL", 0))