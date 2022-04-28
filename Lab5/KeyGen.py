from math import gcd


def functionFi(a, b):
    return (a - 1) * (b - 1)


def prime_check(a):
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def GenerateKeys():
    e = []
    e_open = 0
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    while (prime_check(p) == False) or (prime_check(q) == False):
        print("Error! ENTER PRIME NUMBERS")
        p = int(input("Enter prime number p: "))
        q = int(input("Enter prime number q: "))
    r = p * q
    fi = functionFi(p, q)

    for i in range(2, fi):
        if gcd(i, fi) == 1:
            e.append(i)
    print(f"Введите индекс массива (выбор открытой экспоненты): {e}")
    e_open = e[int(input())]

    div, x, y = gcd_extended(fi, e_open)
    if y < 0:
        y += fi
    K_open = (e_open, r)
    K_close = (y, r)
    return K_open, K_close
