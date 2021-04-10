"""
input : 1s2a
output : saa
"""


def decoding(a):
    count, results = 0, []
    for i in a:
        if i.isdigit():
            count = int(i)
        else:
            results.append(count * i)
            count = 0
    return ''.join(results)


# print(decoding("2r6z"))

a = "rrzzzzzz"
