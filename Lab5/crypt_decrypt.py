def cryptRSA(open_key, text_digit):
    tmp_array = []
    print(open)
    for i in text_digit:
        tmp_array.append(i ** open_key[0] % open_key[1])
    return tmp_array


def decryptRSA(close_key, text_digit):
    tmp_array = []
    print(open)
    for i in text_digit:
        tmp_array.append(i ** close_key[0] % close_key[1])
    return tmp_array
