import unittest


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

    return Hn(num) + \
        (1 if not Hn(num) < 0 else 0) *\
        (Sn(num) + (1 if (not a_Bit(Tn(num-1)) and b_Bit(Tn(num-1))) else 0) * Tn(num-1))


def Rn(num):
    binary = (not (b_Bit(Sn(num)) and b_Bit(Tn(num-1))))
    return abs(Tn(num)) if binary else 0


def Substract():

    A_sub_B = 0
    for num in range(A):
        A_sub_B += Rn(num) << num

    if A_sub_B != (A-B):
        printResult(A_sub_B)


def printResult(A_sub_B):
    print("{0}: {1} {2}".format("A", A, bin(A)))
    print("{0}: {1} {2}".format("B", B, bin(B)))
    print("A - B: {0} {1}".format(A-B, bin(A-B)))
    print("")

    print("result : {0}{1}{2}{3}".format(Rn(3), Rn(2), Rn(1), Rn(0)))

    print(A_sub_B == (A-B))
    print(bin(A_sub_B))


if __name__ == '__main__':
    # A-B  (A>B)
    
    A=1021
    B=365

    # MAX_NUM = 1024
    # for A in range(MAX_NUM+1):
    #     for B in range(A/2, A+1):
    #         Substract()
    #     print(A)

    print()
    print("Done")
