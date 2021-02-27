# this program checks if the given number is a power of 2

def power_of_2(number):
    result = (number & (number - 1) == 0)
    if result:
        print("It is a power of 2.")
    else:
        print("It is not power of 2.")


power_of_2(45)
