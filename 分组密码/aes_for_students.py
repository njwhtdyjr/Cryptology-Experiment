N_ROUNDS = 10
Nk = 4

BYTE_MASK = 0xFF
WORD_MASK = 0xFFFFFFFF

key_hex = 0x2B7E151628AED2A6ABF7158809CF4F3C
input_hex = 0x3243F6A8885A308D313198A2E0370734

# key_hex = 0x000102030405060708090A0B0C0D0E0F
# input_hex = 0x00112233445566778899AABBCCDDEEFF


def hex2matrix(num):
    res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # TODO
    for i in range(16):
        res[i % 4][i // 4] = (num >> (120 - i * 8)) & BYTE_MASK
    return res


def matrix2hex(s):
    res = 0
    # TODO
    for i in range(16):
        res = res | (s[i % 4][i // 4] << (120 - i * 8))
    return res


def key2words(key):
    keycolunms = []
    # TODO
    for i in range(4):
        keycolunms.append((key >> (96 - i * 32)) & WORD_MASK)
    return keycolunms


def shift_rows(s):
    # TODO
    for i in range(4):
        s[i] = s[i][i:] + s[i][:i]


def inv_shift_rows(s):
    # TODO
    for i in range(4):
        s[i] = s[i][-i:] + s[i][:-i]


def xtime(a):
    return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else ((a << 1) & 0xFF)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    # TODO
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        l = [s[0][i], s[1][i], s[2][i], s[3][i]]
        mix_single_column(l)
        s[0][i], s[1][i], s[2][i], s[3][i] = l[0], l[1], l[2], l[3]


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    # TODO
    for i in range(4):
        u = xtime(xtime(s[0][i] ^ s[2][i]))
        v = xtime(xtime(s[1][i] ^ s[3][i]))
        s[0][i] ^= u
        s[1][i] ^= v
        s[2][i] ^= u
        s[3][i] ^= v
    mix_columns(s)
def add_round_key(s, k):
    news = s
    # TODO
    for i in range(4):
        for j in range(4):
            news[j][i] = s[j][i] ^ ((k[i] >> (24 - j * 8)) & BYTE_MASK)
    return news


s_box = (
    0x63,
    0x7C,
    0x77,
    0x7B,
    0xF2,
    0x6B,
    0x6F,
    0xC5,
    0x30,
    0x01,
    0x67,
    0x2B,
    0xFE,
    0xD7,
    0xAB,
    0x76,
    0xCA,
    0x82,
    0xC9,
    0x7D,
    0xFA,
    0x59,
    0x47,
    0xF0,
    0xAD,
    0xD4,
    0xA2,
    0xAF,
    0x9C,
    0xA4,
    0x72,
    0xC0,
    0xB7,
    0xFD,
    0x93,
    0x26,
    0x36,
    0x3F,
    0xF7,
    0xCC,
    0x34,
    0xA5,
    0xE5,
    0xF1,
    0x71,
    0xD8,
    0x31,
    0x15,
    0x04,
    0xC7,
    0x23,
    0xC3,
    0x18,
    0x96,
    0x05,
    0x9A,
    0x07,
    0x12,
    0x80,
    0xE2,
    0xEB,
    0x27,
    0xB2,
    0x75,
    0x09,
    0x83,
    0x2C,
    0x1A,
    0x1B,
    0x6E,
    0x5A,
    0xA0,
    0x52,
    0x3B,
    0xD6,
    0xB3,
    0x29,
    0xE3,
    0x2F,
    0x84,
    0x53,
    0xD1,
    0x00,
    0xED,
    0x20,
    0xFC,
    0xB1,
    0x5B,
    0x6A,
    0xCB,
    0xBE,
    0x39,
    0x4A,
    0x4C,
    0x58,
    0xCF,
    0xD0,
    0xEF,
    0xAA,
    0xFB,
    0x43,
    0x4D,
    0x33,
    0x85,
    0x45,
    0xF9,
    0x02,
    0x7F,
    0x50,
    0x3C,
    0x9F,
    0xA8,
    0x51,
    0xA3,
    0x40,
    0x8F,
    0x92,
    0x9D,
    0x38,
    0xF5,
    0xBC,
    0xB6,
    0xDA,
    0x21,
    0x10,
    0xFF,
    0xF3,
    0xD2,
    0xCD,
    0x0C,
    0x13,
    0xEC,
    0x5F,
    0x97,
    0x44,
    0x17,
    0xC4,
    0xA7,
    0x7E,
    0x3D,
    0x64,
    0x5D,
    0x19,
    0x73,
    0x60,
    0x81,
    0x4F,
    0xDC,
    0x22,
    0x2A,
    0x90,
    0x88,
    0x46,
    0xEE,
    0xB8,
    0x14,
    0xDE,
    0x5E,
    0x0B,
    0xDB,
    0xE0,
    0x32,
    0x3A,
    0x0A,
    0x49,
    0x06,
    0x24,
    0x5C,
    0xC2,
    0xD3,
    0xAC,
    0x62,
    0x91,
    0x95,
    0xE4,
    0x79,
    0xE7,
    0xC8,
    0x37,
    0x6D,
    0x8D,
    0xD5,
    0x4E,
    0xA9,
    0x6C,
    0x56,
    0xF4,
    0xEA,
    0x65,
    0x7A,
    0xAE,
    0x08,
    0xBA,
    0x78,
    0x25,
    0x2E,
    0x1C,
    0xA6,
    0xB4,
    0xC6,
    0xE8,
    0xDD,
    0x74,
    0x1F,
    0x4B,
    0xBD,
    0x8B,
    0x8A,
    0x70,
    0x3E,
    0xB5,
    0x66,
    0x48,
    0x03,
    0xF6,
    0x0E,
    0x61,
    0x35,
    0x57,
    0xB9,
    0x86,
    0xC1,
    0x1D,
    0x9E,
    0xE1,
    0xF8,
    0x98,
    0x11,
    0x69,
    0xD9,
    0x8E,
    0x94,
    0x9B,
    0x1E,
    0x87,
    0xE9,
    0xCE,
    0x55,
    0x28,
    0xDF,
    0x8C,
    0xA1,
    0x89,
    0x0D,
    0xBF,
    0xE6,
    0x42,
    0x68,
    0x41,
    0x99,
    0x2D,
    0x0F,
    0xB0,
    0x54,
    0xBB,
    0x16,
)

inv_s_box = (
    0x52,
    0x09,
    0x6A,
    0xD5,
    0x30,
    0x36,
    0xA5,
    0x38,
    0xBF,
    0x40,
    0xA3,
    0x9E,
    0x81,
    0xF3,
    0xD7,
    0xFB,
    0x7C,
    0xE3,
    0x39,
    0x82,
    0x9B,
    0x2F,
    0xFF,
    0x87,
    0x34,
    0x8E,
    0x43,
    0x44,
    0xC4,
    0xDE,
    0xE9,
    0xCB,
    0x54,
    0x7B,
    0x94,
    0x32,
    0xA6,
    0xC2,
    0x23,
    0x3D,
    0xEE,
    0x4C,
    0x95,
    0x0B,
    0x42,
    0xFA,
    0xC3,
    0x4E,
    0x08,
    0x2E,
    0xA1,
    0x66,
    0x28,
    0xD9,
    0x24,
    0xB2,
    0x76,
    0x5B,
    0xA2,
    0x49,
    0x6D,
    0x8B,
    0xD1,
    0x25,
    0x72,
    0xF8,
    0xF6,
    0x64,
    0x86,
    0x68,
    0x98,
    0x16,
    0xD4,
    0xA4,
    0x5C,
    0xCC,
    0x5D,
    0x65,
    0xB6,
    0x92,
    0x6C,
    0x70,
    0x48,
    0x50,
    0xFD,
    0xED,
    0xB9,
    0xDA,
    0x5E,
    0x15,
    0x46,
    0x57,
    0xA7,
    0x8D,
    0x9D,
    0x84,
    0x90,
    0xD8,
    0xAB,
    0x00,
    0x8C,
    0xBC,
    0xD3,
    0x0A,
    0xF7,
    0xE4,
    0x58,
    0x05,
    0xB8,
    0xB3,
    0x45,
    0x06,
    0xD0,
    0x2C,
    0x1E,
    0x8F,
    0xCA,
    0x3F,
    0x0F,
    0x02,
    0xC1,
    0xAF,
    0xBD,
    0x03,
    0x01,
    0x13,
    0x8A,
    0x6B,
    0x3A,
    0x91,
    0x11,
    0x41,
    0x4F,
    0x67,
    0xDC,
    0xEA,
    0x97,
    0xF2,
    0xCF,
    0xCE,
    0xF0,
    0xB4,
    0xE6,
    0x73,
    0x96,
    0xAC,
    0x74,
    0x22,
    0xE7,
    0xAD,
    0x35,
    0x85,
    0xE2,
    0xF9,
    0x37,
    0xE8,
    0x1C,
    0x75,
    0xDF,
    0x6E,
    0x47,
    0xF1,
    0x1A,
    0x71,
    0x1D,
    0x29,
    0xC5,
    0x89,
    0x6F,
    0xB7,
    0x62,
    0x0E,
    0xAA,
    0x18,
    0xBE,
    0x1B,
    0xFC,
    0x56,
    0x3E,
    0x4B,
    0xC6,
    0xD2,
    0x79,
    0x20,
    0x9A,
    0xDB,
    0xC0,
    0xFE,
    0x78,
    0xCD,
    0x5A,
    0xF4,
    0x1F,
    0xDD,
    0xA8,
    0x33,
    0x88,
    0x07,
    0xC7,
    0x31,
    0xB1,
    0x12,
    0x10,
    0x59,
    0x27,
    0x80,
    0xEC,
    0x5F,
    0x60,
    0x51,
    0x7F,
    0xA9,
    0x19,
    0xB5,
    0x4A,
    0x0D,
    0x2D,
    0xE5,
    0x7A,
    0x9F,
    0x93,
    0xC9,
    0x9C,
    0xEF,
    0xA0,
    0xE0,
    0x3B,
    0x4D,
    0xAE,
    0x2A,
    0xF5,
    0xB0,
    0xC8,
    0xEB,
    0xBB,
    0x3C,
    0x83,
    0x53,
    0x99,
    0x61,
    0x17,
    0x2B,
    0x04,
    0x7E,
    0xBA,
    0x77,
    0xD6,
    0x26,
    0xE1,
    0x69,
    0x14,
    0x63,
    0x55,
    0x21,
    0x0C,
    0x7D,
)


def sub_bytes(s, sbox=s_box):
    news = s
    # TODO
    for i in range(4):
        for j in range(4):
            news[i][j] = sbox[news[i][j]]
    return news


def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00,
        0x01,
        0x02,
        0x04,
        0x08,
        0x10,
        0x20,
        0x40,
        0x80,
        0x1B,
        0x36,
        0x6C,
        0xD8,
        0xAB,
        0x4D,
        0x9A,
        0x2F,
        0x5E,
        0xBC,
        0x63,
        0xC6,
        0x97,
        0x35,
        0x6A,
        0xD4,
        0xB3,
        0x7D,
        0xFA,
        0xEF,
        0xC5,
        0x91,
        0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = key2words(master_key)

    iteration_size = 4
    # TODO
    for i in range(4, 4 * (N_ROUNDS + 1)):
        temp = key_columns[i - 1]
        # print(hex(temp))
        if i % Nk == 0:
            temp = (temp << 8 | temp >> 24) & WORD_MASK
            # print(hex(temp))
            temp1 = 0
            for j in range(4):
                temp1 = (
                    s_box[(temp >> (24 - j * 8)) & BYTE_MASK] << (24 - j * 8)
                ) | temp1
            # print(hex(temp1))
            temp = temp1 ^ ((r_con[i // Nk] << 24) & WORD_MASK)
            # print(hex(temp))
        # print(hex(key_columns[i - Nk]))
        # print(hex(key_columns[i - Nk]^temp))
        key_columns.append(key_columns[i - Nk] ^ temp)
    return key_columns


def printStateinhex(state):
    for word in state:
        print("[{}]".format(", ".join(hex(x) for x in word)))


def encrypt(key, plaintext):
    round_keys = expand_key(key)
    state = hex2matrix(plaintext)
    # TODO
    # Initial add round key step
    state = add_round_key(state, round_keys[:4])
    # printStateinhex(state)
    # print('------------------')
    for i in range(1, N_ROUNDS):
        state = sub_bytes(state)
        # printStateinhex(state)
        # print('------------------')
        shift_rows(state)
        # printStateinhex(state)
        # print('------------------')
        mix_columns(state)
        # printStateinhex(state)
        # print('------------------')
        state = add_round_key(state, round_keys[4 * i : 4 * (i + 1)])
        # printStateinhex(state)
        # print('------------------')
    # Run final round (skips the MixColumns step)
    state = sub_bytes(state)
    shift_rows(state)
    state = add_round_key(state, round_keys[4 * N_ROUNDS : 4 * (N_ROUNDS + 1)])
    printStateinhex(state)
    # print('------------------')
    ciphertext = matrix2hex(state)
    return ciphertext


def decrypt(key, ciphertext):
    # Remember to start from the last round key and work backwards through them when decrypting
    round_keys = expand_key(key)

    # Convert ciphertext to state matrix
    state = hex2matrix(ciphertext)

    # TODO
    # Initial add round key step
    state = add_round_key(state, round_keys[4 * N_ROUNDS : 4 * (N_ROUNDS + 1)])
    # print(hex(matrix2hex(state)))
    for i in range(N_ROUNDS - 1, 0, -1):
        inv_shift_rows(state)
        # print(hex(matrix2hex(state)))
        state = sub_bytes(state, inv_s_box)
        # print(hex(matrix2hex(state)))
        # print(hex(matrix2hex(state)))
        state = add_round_key(state, round_keys[4 * i : 4 * (i + 1)])
        # print(hex(matrix2hex(state)))
        inv_mix_columns(state)
        # print(hex(matrix2hex(state)))
    # Run final round (skips the InvMixColumns step)
    inv_shift_rows(state)
    state = sub_bytes(state, inv_s_box)
    state = add_round_key(state, round_keys[:4])
    # print(hex(matrix2hex(state)))
    printStateinhex(state)
    # print('------------------')

    # Convert state matrix to plaintext
    plaintext = matrix2hex(state)
    return plaintext


ciphertext = encrypt(key_hex, input_hex)
print(f"Encrypted: {(ciphertext):#034X}")


decrypted = decrypt(key_hex, ciphertext)
print(f"Decrypted: {(decrypted):#034X}")
