# this file illustrates the logic of multiplication of two numbers without using
# arithmetic operators

# This uses bitwise add and shift logic
# Time Complexity : O(n^2)

def multiply(x, y):
    def add(a, b):
        running_sum, carry_in, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carry_out = (ak & bk) | (ak & carry_in) | (bk & carry_in)
            running_sum = running_sum | ak ^ bk ^ carry_in
            carry_in, k, temp_a, temp_b = (carry_out << 1, k << 1, temp_a >> 1, temp_b >> 1)

        return running_sum | carry_in

    running_sum = 0
    while x:  # examines each bit of x
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

print(multiply(2,3))
