from rules import *

S1 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]
S2 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


def rebuiltByRule(array, rule):
    new_part = []
    for i in rule:
        new_part.append(array[i])
    return new_part


def XOR(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            str1[i] = "1"
        else:
            str1[i] = "0"
    return str1


def binary(XOR_val, matrix1):
    string = int("".join(XOR_val[::len(XOR_val) - 1]), 2)
    column = int("".join(XOR_val[1:3]), 2)
    int_bin = format(matrix1[string][column], "b").zfill(2)
    return int_bin


def Round(array, key, matrix1, matrix2):
    left = array[:4]
    right = list(array[4:])
    new_part = rebuiltByRule(right, EP)
    X_OR = XOR(new_part, key)
    left_XOR = X_OR[:4]
    right_XOR = X_OR[4:]
    full_string1 = rebuiltByRule(binary(left_XOR, matrix1) + binary(right_XOR, matrix2), P4)
    full_string1 = XOR(list(full_string1), left) + right
    return full_string1


def SDES(mainArray, key1, key2):
    tmp = []
    for i in IP:
        tmp.append(mainArray[i])
    tmp = Round(tmp, key1, S1, S2)
    left = tmp[:4]
    right = tmp[4:]
    tmp = right + left
    tmp = Round(tmp, key2, S1, S2)
    tmp = rebuiltByRule(tmp, IP1)
    return tmp


def DecryptSDES(mainArray, key1, key2):
    mainArray = Round(rebuiltByRule(mainArray, IP), key2, S1, S2)
    left = mainArray[:4]
    right = mainArray[4:]
    mainArray = Round(right + left, key1, S1, S2)
    return rebuiltByRule(mainArray,IP1)
