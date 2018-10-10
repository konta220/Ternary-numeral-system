import unittest

# A-B  (A>B)

# 0b00111
A = 7

# 0b00011
B = 3

# bit count
N = 0
MAX = 5


def a_Bit(num):
    return num > 0


def b_Bit(num):
    return num < 0


def Sn(num):
    return ((A & (1 << num)) >> num) - ((B & (1 << num)) >> num)


def Hn(num):
    if (not ((not a_Bit(Tn(num - 1))) and b_Bit(Tn(num - 1)))):
        return 0

    if (not ((not a_Bit(Sn(num)) and b_Bit(Sn(num))))):
        return 0

    return -1


def Tn(num):
    if num < 0:
        return 0

    return -(1 if Hn(num) < 0 else 0) + \
        (0 if Hn(num) < 0 else 1) *\
        (Sn(num) + (1 if (not a_Bit(Tn(num-1) * b_Bit(num-1))) else 0) * Tn(num-1))


def Rn(num):
    return abs(Tn(num)) if (a_Bit(Tn(num-1)) or (not b_Bit(Tn(num-1)))) else 0


if __name__ == '__main__':
    print("{0}: {1} {2}".format("A", A, bin(A)))
    print("{0}: {1} {2}".format("B", B, bin(B)))
    print("A - B: {0} {1}".format(A-B, bin(A-B)))
    print("")

    print("result")
    print(Rn(3))
    print(Rn(2))
    print(Rn(1))
    print(Rn(0))
