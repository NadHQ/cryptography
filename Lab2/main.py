from KeyGen import KeyGenerate
from Krypt import SDES, DecryptSDES


def main():
    K_key = "1001010011"
    M = "10110110"
    K1, K2 = KeyGenerate(K_key)
    print("----------------------------------------------------------------->")
    print(f"K1:{K1}\n", f"K2:{K2}\n", f"M:{M}\n")
    print("Исходное изображение: " + M)
    cryptMassage = SDES(M, K1, K2)
    print("Зашифрованное сообщение: " + str(cryptMassage))
    decryptMassage = DecryptSDES(cryptMassage, K1, K2)
    print("Дешифрованное сообщение: " + str(decryptMassage))


if __name__ == '__main__':
    main()
