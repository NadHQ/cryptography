import numpy as np

original_word = "cryptography"
crypt_word = ""
key = 3
# crypto_table = crypto_table.astype(str)
part1 = ""
part2 = ""
part3 = ""


def crypt1(original_word):
    crypto_table = np.zeros((key, len(original_word)), dtype=str)
    crypt_word = ""
    for i in range(0, len(original_word)+1, 4):
        for j in range(3):
            crypto_table[j][i + j] = original_word[j + i]

    for i in range(3, len(original_word)+1, 4):
        crypto_table[1][i] = original_word[i]

    for i in range(3):
        for j in range(len(original_word)):
            if (crypto_table[i][j] != ""):
                crypt_word = crypt_word + crypto_table[i][j]

    print(original_word)
    print(crypto_table)
    print(crypt_word)
    return crypt_word


def decrypt1(word, key):
    decrypt1_table = np.zeros((key, len(word)), dtype=str)
    print(decrypt1_table)
    # for i in range(key):
    #     for j in range(0,len(word),):

    return 1


crypt_word = crypt1(original_word)
decrypt_word = decrypt1(crypt_word,key)