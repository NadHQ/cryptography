from KeyGen import *
from crypt_decrypt import *
import string

begin = ""
crypt = ""
encrypt = ""


def from_dig_to_str(rev_dict, message):
    tmp_str = ""
    for i in message:
        tmp_str += rev_dict[i]
    return tmp_str


def main():
    K_open, K_close = GenerateKeys()
    print('Открытый и закрытий ключи: ', K_open, K_close)
    our_dict = {list(string.ascii_letters)[f]: v for f, v in zip(range(53), range(2, 54))}
    our_reverse_dict = {v: list(string.ascii_letters)[f] for v, f in zip(range(2, 54), range(53))}
    begin = input("Введите строку: ")
    my_text_digit = [our_dict[begin[i]] for i in range(len(begin))]
    crypt_digit = cryptRSA(K_open, my_text_digit)
    encrypt_digit = decryptRSA(K_close, crypt_digit)
    crypt = from_dig_to_str(our_reverse_dict, crypt_digit)
    encrypt = from_dig_to_str(our_reverse_dict, encrypt_digit)

    print("Начальный текст:" + begin, "Зашифрованный текст: " + crypt, "Расшифрованный текст: " + encrypt)


if __name__ == '__main__':
    main()
