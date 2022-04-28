def fnv32a(str):
    hval = 0x811c9dc5
    fnv_32_prime = 0x01000193
    uint32_max = 2 ** 32
    for s in str:
        hval = hval ^ s
        hval = (hval * fnv_32_prime) % uint32_max
    return hval


def hashObr(arr, n):
    hO = 100
    for i in arr:
        hO = ((hO + i) ** 2) % n
    return hO

