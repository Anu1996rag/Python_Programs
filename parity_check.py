# this file checks the parity of the word

def parity(word):
    result = 0
    while word:
        result ^= word & 1
        word >>= 1

    if result == 0:
        print("odd parity word")
    else:
        print("even parity word.")

parity(1001)