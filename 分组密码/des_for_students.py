LB32_MASK = 0x00000001
LB64_MASK = 0x0000000000000001
L64_MASK = 0x00000000ffffffff
H64_MASK = 0xffffffff00000000

# Initial Permutation Table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Inverse Initial Permutation Table
PI = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

# Expansion table
E = [
    32,  1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Post P-Box permutation
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# The S-Box tables
S = [
    # S1
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ],
    # S2
    [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ],
    # S3
    [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ],
    # S4
    [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ],
    # S5
    [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],
    # S6
    [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ],
    # S7
    [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ],
    # S8
    [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    ]
]

# Permuted Choice 1 Table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permuted Choice 2 Table
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Iteration Shift Array
iteration_shift = [
    # 1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
    1,  1,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  1
]


# Initial permutation
def initial_permutaion(block):
    init_perm_res = 0
    # TODO
    # 数据从
    for i in range(64):
        init_perm_res += 2**(63-i)*((block >> (64-IP[i])) & LB64_MASK)
    return init_perm_res


# key schedule function
def key_schedule(key):
    Round_key = [0] * 16
    # TODO
    after_PC_1 = 0
    for i in range(56):
        after_PC_1 += 2**(55-i)*((key>>(64-PC1[i]))& LB64_MASK)
    D = after_PC_1 & 0xfffffff
    C = after_PC_1 & 0xfffffff0000000
    for i in range(16):
        D = D & 0xfffffff
        D = ((D >> 28-iteration_shift[i]) | (D << iteration_shift[i])) & 0xfffffff
        C = C & 0xfffffff0000000
        C = ((C >> 28-iteration_shift[i]) | (C << iteration_shift[i])) & 0xfffffff0000000
        CD = (C | D)
        after_PC_2 = 0
        for j in range(48):
            after_PC_2 += 2**(47-j)*((CD>>(56-PC2[j]))& LB64_MASK)
        Round_key[i] = after_PC_2
    return Round_key


def f(R, K):
    f_function_res = 0
    # TODO

    # expansion P-box
    after_expansion_R = 0
    # out多少位数，range就多少。xx-x[i]，xx看in多少位数
    for i in range(48):
        after_expansion_R += 2**(47-i)*((R>>(32-E[i]))& LB32_MASK)
    # XOR K
    after_XOR = after_expansion_R ^ K
    # S BOX
    S_1 = (after_XOR >> 42) & 0x3f
    S_2 = (after_XOR >> 36) & 0x3f
    S_3 = (after_XOR >> 30) & 0x3f
    S_4 = (after_XOR >> 24) & 0x3f
    S_5 = (after_XOR >> 18) & 0x3f
    S_6 = (after_XOR >> 12) & 0x3f
    S_7 = (after_XOR >> 6) & 0x3f
    S_8 = after_XOR & 0x3f

    S_1 = S[0][(((((S_1>>4) & 0x2) | (S_1 & 0x1)) << 4) | ((S_1>>1) & 0xf ))]
    S_2 = S[1][(((((S_2>>4) & 0x2) | (S_2 & 0x1)) << 4) | ((S_2>>1) & 0xf ))]
    S_3 = S[2][(((((S_3>>4) & 0x2) | (S_3 & 0x1)) << 4) | ((S_3>>1) & 0xf ))]
    S_4 = S[3][(((((S_4>>4) & 0x2) | (S_4 & 0x1)) << 4) | ((S_4>>1) & 0xf ))]
    S_5 = S[4][(((((S_5>>4) & 0x2) | (S_5 & 0x1)) << 4) | ((S_5>>1) & 0xf ))]
    S_6 = S[5][(((((S_6>>4) & 0x2) | (S_6 & 0x1)) << 4) | ((S_6>>1) & 0xf ))]
    S_7 = S[6][(((((S_7>>4) & 0x2) | (S_7 & 0x1)) << 4) | ((S_7>>1) & 0xf ))]
    S_8 = S[7][(((((S_8>>4) & 0x2) | (S_8 & 0x1)) << 4) | ((S_8>>1) & 0xf ))]

    after_S_Box = (S_1 << 28) | (S_2 << 24) | (S_3 << 20) | (S_4 << 16) | (S_5 << 12) | (S_6 << 8) | (S_7 << 4) | S_8

    # straight P BOX
    for i in range(32):
        f_function_res += 2**(31-i)*((after_S_Box>>(32-P[i]))& LB32_MASK)
    return f_function_res


def inverse_initial_permutation(block):
    # Inverse initial permutation
    inv_init_perm_res = 0

    # TODO
    for i in range(64):
        inv_init_perm_res += 2**(63-i)*((block >> (64-PI[i])) & LB64_MASK)
    return inv_init_perm_res

# Des Encryption
def des_encrypt(plain, key):
    # TODO

    # round key generation
    Round_key = key_schedule(key)
    # Initial permutation
    after_IP = initial_permutaion(plain)
    # 16 ROUND Feistel
    L = after_IP & H64_MASK
    L = L >> 32
    R = after_IP & L64_MASK
    for i in range(16):
        L = L ^ f(R, Round_key[i])
        L, R = R, L
    L, R = R, L
    print(f"feistel: {((L<<32)|R):016X}")
    # inverse_initial_permutation
    after_inv_IP = inverse_initial_permutation((L << 32) | R)
    return after_inv_IP

# Des Decryption
def des_decrypt(plain, key):
    # TODO

    # round key generation
    Round_key = key_schedule(key)
    # Initial permutation
    after_IP = initial_permutaion(plain)
    # 16 ROUND Feistel
    L = after_IP & H64_MASK
    L = L >> 32
    R = after_IP & L64_MASK
    for i in range(16):
        L = L ^ f(R, Round_key[15-i])
        L, R = R, L
    L, R = R, L
    # inverse_initial_permutation
    after_inv_IP = inverse_initial_permutation((L << 32) | R)
    return after_inv_IP

def test1():
    plain = 0x0123456789ABCDEF
    key   = 0xFEDCBA9876543210

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')

def test2():
    plain = 0x0123456789ABCDEF
    key   = 0x1111111111111111

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')
def test3():
    plain = 0x1111111111111111
    key = 0x1111111111111111

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')
def test4():
    plain = 0x1111111111111111
    key = 0x0123456789ABCDEF

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')
def test5():
    plain = 0x1000000000000001
    key = 0x3000000000000000

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')
def test6():
    plain = 0xFFFFFFFFFFFFFFFF
    key = 0xFFFFFFFFFFFFFFFF

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')
def test7():
    plain = 0x0000000000000000
    key = 0x0000000000000000

    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016X}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016X}')
if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
