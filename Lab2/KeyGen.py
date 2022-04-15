from rules import *

def KeyGenerate(key):
    newKey = []
    K1 = []
    K2 = []
    string = ""
    for i in P10:
        newKey.append(key[i])
    print("GENERATED KEY: " + string.join(newKey))

    """ ГЕНЕРАЦИЯ СДВИНУТОГО КЛЮЧА """
    left = Shift(newKey[:5])
    right = Shift(newKey[5:10])
    print("LEFT:" + str(left))
    print("RIGHT: " + str(right))
    ShiftList = left + right  # СДВИНУТЫЙ СПИСОК
    print("ShiftList: " + str(ShiftList))
    ShiftKey = "".join([i for i in ShiftList])  # СДВИНУТЫЙ КЛЮЧ
    """-----------------------------------------------------------------"""

    """ GENERATE K1 """
    for i in P8:
        K1.append(ShiftKey[i])
    print("K1: " + str(K1))
    """-----------------------------------------------------------------"""

    """GENERATE K2"""
    for i in range(2):
        left = Shift(ShiftList[:5])
        right = Shift(ShiftList[5:10])
        ShiftList = left + right
    ShiftKey = "".join([i for i in ShiftList])
    print(ShiftKey)
    for i in P8:
        K2.append(ShiftKey[i])
    K1str = "".join(K1)
    K2str = "".join(K2)
    """-----------------------------------------------------------------"""

    return K1str, K2str


def Shift(array):
    tmp = array[0]
    array.pop(0)
    array.append(tmp[0])
    return array