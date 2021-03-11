# this file is used to compute x^y
# x is a double and y is an integer

def power(x, y):
    result, power = 1.0, y

    if y < 0: # if the power is negative
        power, x = -power, 1.0 / x
    while power:
        if power & 1: #odd numbers in power (1,3,5,...)
            result = result * x
        x = x * x
        power = power >> 1
    return result

print(power(2.2,5))
