""" if the input is [1,2,9] then increment the no by 1,
    it will be like 129+1 which is equal to 130 and return
    the value as [1,3,0]"""


def plus_one(array_input):
    array_input[-1] += 1

    for i in reversed(range(1, len(array_input))):
        if array_input[i] != 10:
            break
        array_input[i] = 0
        array_input[i - 1] += 1

    if array_input[0] == 10:
        # if there is a carry out, we need space or one more digit to store the result
        # to do this, append a 0 at the end of the array
        # and update the first entry to 1
        array_input[0] = 1
        array_input.append(0)

    return array_input


print(plus_one([1, 9, 9]))
