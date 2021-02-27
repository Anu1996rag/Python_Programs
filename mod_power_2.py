# this program divides any number with the number having power of 2
# returns the remainder
# example : 35 % 16(2^4) = 3

def mod_power_2(number, power):
    return number & ((1 << power) - 1)


print(mod_power_2(35, 2))
