""" this programs illustrates programs on  array
    Time Complexity : O(n)
    Space Complexity : O(1)
"""

a = [1, 3, 0, 2, 4]

farthest_reach, last_index = 0, len(a) - 1
i = 0

while i <= farthest_reach < last_index:  # i <= farthest_reach and farthest_reach < last_index
    farthest_reach = max(farthest_reach, a[i] + i)
    i += 1
    if farthest_reach >= last_index:
        break

"""
Deleting duplicate entries from a sorted array
"""


def delete_duplicates(array_input):
    if not array_input:
        return 0

    write_index = 1
    for i in range(1, len(array_input)):
        if array_input[write_index - 1] != array_input[i]:
            array_input[write_index] = array_input[i]
            write_index += 1
        print("After incrementing each write index , array is :", array_input)
    return write_index


# print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))

# print(list({2, 3, 5, 5, 7, 11, 11, 11, 13}))


def delete_duplicates_with_element(array_input, key):
    """
    deletes only one occurrence of the key
    :param array_input:
    :param key:
    :return: array with one duplicate element deleted
    """
    if not array_input:
        return 0

    # write_index = 1
    for i in range(len(array_input)):
        if array_input[i] == key:
            array_input[i] = array_input[i + 1]

        print("After incrementing each write index , array is :", array_input)
    return array_input


# print(delete_duplicates_with_element([2, 3, 5, 5, 7, 11, 11, 11, 13], 5))

def delete_duplicates_from_list(array_input):
    """
    keeps only one occurrence of the elements
    :param array_input:
    :param key:
    :return: temp array with duplicate elements deleted
    """
    if not array_input:
        return 0

    temp_list = []
    for i in array_input:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


# print(delete_duplicates_from_list([2, 3, 5, 5, 7, 11, 11, 11, 13]))

def delete_duplicates_from_list_with_key(array_input, key):
    """
    keeps only one occurrence of the elements
    :param array_input:
    :param key:
    :return: temp array with duplicate elements deleted
    """
    if not array_input:
        return 0

    temp_list = []
    for i in range(len(array_input)):
        if array_input[i] != key:
            temp_list.append(array_input[i])
    return temp_list


# print(delete_duplicates_from_list_with_key([2, 3, 5, 5, 7, 11, 11, 11, 13],11))

def buy_and_sell_stock_once(A):
    # first approach
    max_profit = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


def buy_and_sell_stock_once(A):
    # second approach
    min_price = A[0]  # first element
    max_profit = 0.0
    for price in A:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit


# print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

def buy_and_sell_stock_twice(prices):
    if not prices:
        return 0

    # forward phase
    first_profits = []
    min_price, max_profit = float('inf'), 0
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
        first_profits.append(max_profit)
    print("First Profits :", first_profits)
    # backward phase
    max_price = float('-inf')
    for i in reversed(range(1, len(prices))):
        max_price = max(max_price, prices[i])
        print("Max price for backward phase :", max_price)
        max_profit = max(max_profit, first_profits[i - 1] + max_price - prices[i])
        print("First profits in backward phase :", first_profits[i - 1])
        print("Max profit in backward phase :", max_profit)

    return max_profit


# print(buy_and_sell_stock_twice([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

# computing an alternation
a = [0, 1, 2, 3, 4]

# brute-force approach
for i in range(len(a) - 1):
    if i % 2 == 0 and a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]

    if i % 2 != 0 and a[i] < a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]

# second approach
for i in range(len(a)):
    a[i:i + 2] = sorted(a[i:i + 2], reverse=i % 2)

# random sampling
import random

a = [1,2,3,5,6,3,2,1]
for i in range(len(a)):
    r = random.randint(i, len(a)-1)
    a[r],a[i] = a[i],a[r]
print(a)