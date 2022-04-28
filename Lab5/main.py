from KeyGen import *
from crypt_decrypt import *
import string
from hash_func import hashObr

begin = ""
update_begin = "BRUIR"
crypt = ""
encrypt = ""
sign1 = 0
sign2 = 0
our_dict = {list(string.ascii_letters)[f]: v for f, v in zip(range(53), range(2, 54))}
our_reverse_dict = {v: list(string.ascii_letters)[f] for v, f in zip(range(2, 54), range(53))}


def from_dig_to_str(rev_dict, message):
    tmp_str = ""
    for i in message:
        tmp_str += rev_dict[i]
    return tmp_str


def main():
    K_open, K_close = GenerateKeys()
    print('Открытый и закрытий ключи: ', K_open, K_close)

    begin = input("Введите строку: ")

    my_update_digit = [our_dict[update_begin[i]] for i in range(len(update_begin))]
    my_text_digit = [our_dict[begin[i]] for i in range(len(begin))]

    # Формируем хеш образ и подписываем сообщение
    hash_original = hashObr(my_text_digit, K_open[1])
    sign1 = (hash_original ** K_close[0]) % K_close[1]
    # -----------------------------------------------------------

    hash_original_update = hashObr(my_update_digit, K_open[1])  # Хеш образ бруира (сравниваем его с  сигн2)
    sign2 = (sign1 ** K_open[0]) % K_open[1]

    if hash_original_update == sign2:
        print("NORM")
    else:
        print("NOT NORM")
    # encrypt_digit = decryptRSA(K_close, crypt_digit)
    # crypt = from_dig_to_str(our_reverse_dict, crypt_digit)
    # encrypt = from_dig_to_str(our_reverse_dict, encrypt_digit)

    print("Начальный текст:" + begin, "Зашифрованный текст: " + crypt, "Расшифрованный текст: " + encrypt)


if __name__ == '__main__':
    main()
