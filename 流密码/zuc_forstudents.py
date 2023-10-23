# /* the s-boxes */
S0 = [
    0x3E,
    0x72,
    0x5B,
    0x47,
    0xCA,
    0xE0,
    0x00,
    0x33,
    0x04,
    0xD1,
    0x54,
    0x98,
    0x09,
    0xB9,
    0x6D,
    0xCB,
    0x7B,
    0x1B,
    0xF9,
    0x32,
    0xAF,
    0x9D,
    0x6A,
    0xA5,
    0xB8,
    0x2D,
    0xFC,
    0x1D,
    0x08,
    0x53,
    0x03,
    0x90,
    0x4D,
    0x4E,
    0x84,
    0x99,
    0xE4,
    0xCE,
    0xD9,
    0x91,
    0xDD,
    0xB6,
    0x85,
    0x48,
    0x8B,
    0x29,
    0x6E,
    0xAC,
    0xCD,
    0xC1,
    0xF8,
    0x1E,
    0x73,
    0x43,
    0x69,
    0xC6,
    0xB5,
    0xBD,
    0xFD,
    0x39,
    0x63,
    0x20,
    0xD4,
    0x38,
    0x76,
    0x7D,
    0xB2,
    0xA7,
    0xCF,
    0xED,
    0x57,
    0xC5,
    0xF3,
    0x2C,
    0xBB,
    0x14,
    0x21,
    0x06,
    0x55,
    0x9B,
    0xE3,
    0xEF,
    0x5E,
    0x31,
    0x4F,
    0x7F,
    0x5A,
    0xA4,
    0x0D,
    0x82,
    0x51,
    0x49,
    0x5F,
    0xBA,
    0x58,
    0x1C,
    0x4A,
    0x16,
    0xD5,
    0x17,
    0xA8,
    0x92,
    0x24,
    0x1F,
    0x8C,
    0xFF,
    0xD8,
    0xAE,
    0x2E,
    0x01,
    0xD3,
    0xAD,
    0x3B,
    0x4B,
    0xDA,
    0x46,
    0xEB,
    0xC9,
    0xDE,
    0x9A,
    0x8F,
    0x87,
    0xD7,
    0x3A,
    0x80,
    0x6F,
    0x2F,
    0xC8,
    0xB1,
    0xB4,
    0x37,
    0xF7,
    0x0A,
    0x22,
    0x13,
    0x28,
    0x7C,
    0xCC,
    0x3C,
    0x89,
    0xC7,
    0xC3,
    0x96,
    0x56,
    0x07,
    0xBF,
    0x7E,
    0xF0,
    0x0B,
    0x2B,
    0x97,
    0x52,
    0x35,
    0x41,
    0x79,
    0x61,
    0xA6,
    0x4C,
    0x10,
    0xFE,
    0xBC,
    0x26,
    0x95,
    0x88,
    0x8A,
    0xB0,
    0xA3,
    0xFB,
    0xC0,
    0x18,
    0x94,
    0xF2,
    0xE1,
    0xE5,
    0xE9,
    0x5D,
    0xD0,
    0xDC,
    0x11,
    0x66,
    0x64,
    0x5C,
    0xEC,
    0x59,
    0x42,
    0x75,
    0x12,
    0xF5,
    0x74,
    0x9C,
    0xAA,
    0x23,
    0x0E,
    0x86,
    0xAB,
    0xBE,
    0x2A,
    0x02,
    0xE7,
    0x67,
    0xE6,
    0x44,
    0xA2,
    0x6C,
    0xC2,
    0x93,
    0x9F,
    0xF1,
    0xF6,
    0xFA,
    0x36,
    0xD2,
    0x50,
    0x68,
    0x9E,
    0x62,
    0x71,
    0x15,
    0x3D,
    0xD6,
    0x40,
    0xC4,
    0xE2,
    0x0F,
    0x8E,
    0x83,
    0x77,
    0x6B,
    0x25,
    0x05,
    0x3F,
    0x0C,
    0x30,
    0xEA,
    0x70,
    0xB7,
    0xA1,
    0xE8,
    0xA9,
    0x65,
    0x8D,
    0x27,
    0x1A,
    0xDB,
    0x81,
    0xB3,
    0xA0,
    0xF4,
    0x45,
    0x7A,
    0x19,
    0xDF,
    0xEE,
    0x78,
    0x34,
    0x60,
]

S1 = [
    0x55,
    0xC2,
    0x63,
    0x71,
    0x3B,
    0xC8,
    0x47,
    0x86,
    0x9F,
    0x3C,
    0xDA,
    0x5B,
    0x29,
    0xAA,
    0xFD,
    0x77,
    0x8C,
    0xC5,
    0x94,
    0x0C,
    0xA6,
    0x1A,
    0x13,
    0x00,
    0xE3,
    0xA8,
    0x16,
    0x72,
    0x40,
    0xF9,
    0xF8,
    0x42,
    0x44,
    0x26,
    0x68,
    0x96,
    0x81,
    0xD9,
    0x45,
    0x3E,
    0x10,
    0x76,
    0xC6,
    0xA7,
    0x8B,
    0x39,
    0x43,
    0xE1,
    0x3A,
    0xB5,
    0x56,
    0x2A,
    0xC0,
    0x6D,
    0xB3,
    0x05,
    0x22,
    0x66,
    0xBF,
    0xDC,
    0x0B,
    0xFA,
    0x62,
    0x48,
    0xDD,
    0x20,
    0x11,
    0x06,
    0x36,
    0xC9,
    0xC1,
    0xCF,
    0xF6,
    0x27,
    0x52,
    0xBB,
    0x69,
    0xF5,
    0xD4,
    0x87,
    0x7F,
    0x84,
    0x4C,
    0xD2,
    0x9C,
    0x57,
    0xA4,
    0xBC,
    0x4F,
    0x9A,
    0xDF,
    0xFE,
    0xD6,
    0x8D,
    0x7A,
    0xEB,
    0x2B,
    0x53,
    0xD8,
    0x5C,
    0xA1,
    0x14,
    0x17,
    0xFB,
    0x23,
    0xD5,
    0x7D,
    0x30,
    0x67,
    0x73,
    0x08,
    0x09,
    0xEE,
    0xB7,
    0x70,
    0x3F,
    0x61,
    0xB2,
    0x19,
    0x8E,
    0x4E,
    0xE5,
    0x4B,
    0x93,
    0x8F,
    0x5D,
    0xDB,
    0xA9,
    0xAD,
    0xF1,
    0xAE,
    0x2E,
    0xCB,
    0x0D,
    0xFC,
    0xF4,
    0x2D,
    0x46,
    0x6E,
    0x1D,
    0x97,
    0xE8,
    0xD1,
    0xE9,
    0x4D,
    0x37,
    0xA5,
    0x75,
    0x5E,
    0x83,
    0x9E,
    0xAB,
    0x82,
    0x9D,
    0xB9,
    0x1C,
    0xE0,
    0xCD,
    0x49,
    0x89,
    0x01,
    0xB6,
    0xBD,
    0x58,
    0x24,
    0xA2,
    0x5F,
    0x38,
    0x78,
    0x99,
    0x15,
    0x90,
    0x50,
    0xB8,
    0x95,
    0xE4,
    0xD0,
    0x91,
    0xC7,
    0xCE,
    0xED,
    0x0F,
    0xB4,
    0x6F,
    0xA0,
    0xCC,
    0xF0,
    0x02,
    0x4A,
    0x79,
    0xC3,
    0xDE,
    0xA3,
    0xEF,
    0xEA,
    0x51,
    0xE6,
    0x6B,
    0x18,
    0xEC,
    0x1B,
    0x2C,
    0x80,
    0xF7,
    0x74,
    0xE7,
    0xFF,
    0x21,
    0x5A,
    0x6A,
    0x54,
    0x1E,
    0x41,
    0x31,
    0x92,
    0x35,
    0xC4,
    0x33,
    0x07,
    0x0A,
    0xBA,
    0x7E,
    0x0E,
    0x34,
    0x88,
    0xB1,
    0x98,
    0x7C,
    0xF3,
    0x3D,
    0x60,
    0x6C,
    0x7B,
    0xCA,
    0xD3,
    0x1F,
    0x32,
    0x65,
    0x04,
    0x28,
    0x64,
    0xBE,
    0x85,
    0x9B,
    0x2F,
    0x59,
    0x8A,
    0xD7,
    0xB0,
    0x25,
    0xAC,
    0xAF,
    0x12,
    0x03,
    0xE2,
    0xF2,
]

# /* the constants D */
EK_d = [
    0x44D7,
    0x26BC,
    0x626B,
    0x135E,
    0x5789,
    0x35E2,
    0x7135,
    0x09AF,
    0x4D78,
    0x2F13,
    0x6BC4,
    0x1AF1,
    0x5E26,
    0x3C4D,
    0x789A,
    0x47AC,
]

# /* c = a + b mod (2^31 – 1) */
def AddM(a, b):
    # TODO
    c = (a + b) & 0xFFFFFFFF
    return (c & 0x7FFFFFFF) + (c >> 31)


def MulByPow2(x, k):
    return ((x << k) | (x >> (31 - k))) & 0x7FFFFFFF


# /* LFSR with initialization mode */
def LFSRWithInitialisationMode(u):
    global LFSR_S0, LFSR_S1, LFSR_S2, LFSR_S3, LFSR_S4, LFSR_S5, LFSR_S6, LFSR_S7, LFSR_S8, LFSR_S9, LFSR_S10, LFSR_S11, LFSR_S12, LFSR_S13, LFSR_S14, LFSR_S15
    # 按照C语言中的数据类型，对python中的数据进行掩码运算，保证数据类型一致
    # TODO
    LFSR_S0 = LFSR_S0 & 0xFFFFFFFF
    LFSR_S1 = LFSR_S1 & 0xFFFFFFFF
    LFSR_S2 = LFSR_S2 & 0xFFFFFFFF
    LFSR_S3 = LFSR_S3 & 0xFFFFFFFF
    LFSR_S4 = LFSR_S4 & 0xFFFFFFFF
    LFSR_S5 = LFSR_S5 & 0xFFFFFFFF
    LFSR_S6 = LFSR_S6 & 0xFFFFFFFF
    LFSR_S7 = LFSR_S7 & 0xFFFFFFFF
    LFSR_S8 = LFSR_S8 & 0xFFFFFFFF
    LFSR_S9 = LFSR_S9 & 0xFFFFFFFF
    LFSR_S10 = LFSR_S10 & 0xFFFFFFFF
    LFSR_S11 = LFSR_S11 & 0xFFFFFFFF
    LFSR_S12 = LFSR_S12 & 0xFFFFFFFF
    LFSR_S13 = LFSR_S13 & 0xFFFFFFFF
    LFSR_S14 = LFSR_S14 & 0xFFFFFFFF
    LFSR_S15 = LFSR_S15 & 0xFFFFFFFF

    f = LFSR_S0
    v = MulByPow2(LFSR_S0, 8)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S4, 20)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S10, 21)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S13, 17)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S15, 15)
    f = AddM(f, v)

    f = AddM(f, u & 0xFFFFFFFF)

    LFSR_S0 = LFSR_S1
    LFSR_S1 = LFSR_S2
    LFSR_S2 = LFSR_S3
    LFSR_S3 = LFSR_S4
    LFSR_S4 = LFSR_S5
    LFSR_S5 = LFSR_S6
    LFSR_S6 = LFSR_S7
    LFSR_S7 = LFSR_S8
    LFSR_S8 = LFSR_S9
    LFSR_S9 = LFSR_S10
    LFSR_S10 = LFSR_S11
    LFSR_S11 = LFSR_S12
    LFSR_S12 = LFSR_S13
    LFSR_S13 = LFSR_S14
    LFSR_S14 = LFSR_S15
    LFSR_S15 = f


# Make sure to define MulByPow2 and AddM functions as mentioned earlier

# /* LFSR with work mode */
def LFSRWithWorkMode():
    global LFSR_S0, LFSR_S1, LFSR_S2, LFSR_S3, LFSR_S4, LFSR_S5, LFSR_S6, LFSR_S7, LFSR_S8, LFSR_S9, LFSR_S10, LFSR_S11, LFSR_S12, LFSR_S13, LFSR_S14, LFSR_S15

    # TODO
    LFSR_S0 = LFSR_S0 & 0xFFFFFFFF
    LFSR_S1 = LFSR_S1 & 0xFFFFFFFF
    LFSR_S2 = LFSR_S2 & 0xFFFFFFFF
    LFSR_S3 = LFSR_S3 & 0xFFFFFFFF
    LFSR_S4 = LFSR_S4 & 0xFFFFFFFF
    LFSR_S5 = LFSR_S5 & 0xFFFFFFFF
    LFSR_S6 = LFSR_S6 & 0xFFFFFFFF
    LFSR_S7 = LFSR_S7 & 0xFFFFFFFF
    LFSR_S8 = LFSR_S8 & 0xFFFFFFFF
    LFSR_S9 = LFSR_S9 & 0xFFFFFFFF
    LFSR_S10 = LFSR_S10 & 0xFFFFFFFF
    LFSR_S11 = LFSR_S11 & 0xFFFFFFFF
    LFSR_S12 = LFSR_S12 & 0xFFFFFFFF
    LFSR_S13 = LFSR_S13 & 0xFFFFFFFF
    LFSR_S14 = LFSR_S14 & 0xFFFFFFFF
    LFSR_S15 = LFSR_S15 & 0xFFFFFFFF

    f = LFSR_S0
    v = MulByPow2(LFSR_S0, 8)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S4, 20)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S10, 21)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S13, 17)
    f = AddM(f, v)

    v = MulByPow2(LFSR_S15, 15)
    f = AddM(f, v)

    LFSR_S0 = LFSR_S1
    LFSR_S1 = LFSR_S2
    LFSR_S2 = LFSR_S3
    LFSR_S3 = LFSR_S4
    LFSR_S4 = LFSR_S5
    LFSR_S5 = LFSR_S6
    LFSR_S6 = LFSR_S7
    LFSR_S7 = LFSR_S8
    LFSR_S8 = LFSR_S9
    LFSR_S9 = LFSR_S10
    LFSR_S10 = LFSR_S11
    LFSR_S11 = LFSR_S12
    LFSR_S12 = LFSR_S13
    LFSR_S13 = LFSR_S14
    LFSR_S14 = LFSR_S15
    LFSR_S15 = f


# /* BitReorganization */
def BitReorganization():
    global BRC_X0, BRC_X1, BRC_X2, BRC_X3
    global LFSR_S0, LFSR_S1, LFSR_S2, LFSR_S3, LFSR_S4, LFSR_S5, LFSR_S6, LFSR_S7, LFSR_S8, LFSR_S9, LFSR_S10, LFSR_S11, LFSR_S12, LFSR_S13, LFSR_S14, LFSR_S15

    # TODO
    BRC_X0 = ((LFSR_S15 & 0x7FFF8000) << 1) | (LFSR_S14 & 0xFFFF)
    BRC_X1 = ((LFSR_S11 & 0xFFFF) << 16) | (LFSR_S9 >> 15)
    BRC_X2 = ((LFSR_S7 & 0xFFFF) << 16) | (LFSR_S5 >> 15)
    BRC_X3 = ((LFSR_S2 & 0xFFFF) << 16) | (LFSR_S0 >> 15)
    BRC_X0 = BRC_X0 & 0xFFFFFFFF
    BRC_X1 = BRC_X1 & 0xFFFFFFFF
    BRC_X2 = BRC_X2 & 0xFFFFFFFF
    BRC_X3 = BRC_X3 & 0xFFFFFFFF
    # print(BRC_X3)


#     发现BRC_X3的值不对，与C语言作比较，C语言中显示出有符号整数，不好判断Python中的
#     无符号整数是否与C中的一致。不知道为什么，


def ROT(a, k):
    return ((a << k) | (a >> (32 - k))) & 0xFFFFFFFF


def L1(X):
    # TODO
    return (X ^ ROT(X, 2) ^ ROT(X, 10) ^ ROT(X, 18) ^ ROT(X, 24)) & 0xFFFFFFFF


def L2(X):
    # TODO
    return (X ^ ROT(X, 8) ^ ROT(X, 14) ^ ROT(X, 22) ^ ROT(X, 30))& 0xFFFFFFFF


def MAKEU32(a, b, c, d):
    return (
        ((a & 0xFFFFFFFF) << 24)
        | ((b & 0xFFFFFFFF) << 16)
        | ((c & 0xFFFFFFFF) << 8)
        | (d & 0xFFFFFFFF)
    ) & 0xFFFFFFFF


def F():
    global F_R1, F_R2
    # TODO
    F_R1 =F_R1 & 0xFFFFFFFF
    F_R2 =F_R2 & 0xFFFFFFFF

    W = ((BRC_X0 ^ F_R1) + F_R2) & 0xFFFFFFFF
    W1 = (F_R1 + BRC_X1) & 0xFFFFFFFF
    W2 = (F_R2 ^ BRC_X2) & 0xFFFFFFFF
    u = L1(((W1 << 16) | (W2 >> 16)) & 0xFFFFFFFF)
    v = L2(((W2 << 16) | (W1 >> 16)) & 0xFFFFFFFF)
    F_R1 = MAKEU32(S0[u >> 24], S1[(u >> 16) & 0xFF], S0[(u >> 8) & 0xFF], S1[u & 0xFF])
    F_R2 = MAKEU32(S0[v >> 24], S1[(v >> 16) & 0xFF], S0[(v >> 8) & 0xFF], S1[v & 0xFF])
    return W


def MAKEU31(a, b, c):
    return ((a & 0xFFFFFFFF) << 23) | ((b & 0xFFFFFFFF) << 8) | (c & 0xFFFFFFFF)


def Initialization(k, iv):
    global LFSR_S0, LFSR_S1, LFSR_S2, LFSR_S3, LFSR_S4, LFSR_S5, LFSR_S6, LFSR_S7, LFSR_S8, LFSR_S9, LFSR_S10, LFSR_S11, LFSR_S12, LFSR_S13, LFSR_S14, LFSR_S15, F_R1, F_R2
    # print(k,EK_d,iv)
    # TODO
    LFSR_S0 = MAKEU31(k[0], EK_d[0], iv[0])
    LFSR_S1 = MAKEU31(k[1], EK_d[1], iv[1])
    LFSR_S2 = MAKEU31(k[2], EK_d[2], iv[2])
    LFSR_S3 = MAKEU31(k[3], EK_d[3], iv[3])
    LFSR_S4 = MAKEU31(k[4], EK_d[4], iv[4])
    LFSR_S5 = MAKEU31(k[5], EK_d[5], iv[5])
    LFSR_S6 = MAKEU31(k[6], EK_d[6], iv[6])
    LFSR_S7 = MAKEU31(k[7], EK_d[7], iv[7])
    LFSR_S8 = MAKEU31(k[8], EK_d[8], iv[8])
    LFSR_S9 = MAKEU31(k[9], EK_d[9], iv[9])
    LFSR_S10 = MAKEU31(k[10], EK_d[10], iv[10])
    LFSR_S11 = MAKEU31(k[11], EK_d[11], iv[11])
    LFSR_S12 = MAKEU31(k[12], EK_d[12], iv[12])
    LFSR_S13 = MAKEU31(k[13], EK_d[13], iv[13])
    LFSR_S14 = MAKEU31(k[14], EK_d[14], iv[14])
    LFSR_S15 = MAKEU31(k[15], EK_d[15], iv[15])

    LFSR_S0 = LFSR_S0 & 0xFFFFFFFF
    LFSR_S1 = LFSR_S1 & 0xFFFFFFFF
    LFSR_S2 = LFSR_S2 & 0xFFFFFFFF
    LFSR_S3 = LFSR_S3 & 0xFFFFFFFF
    LFSR_S4 = LFSR_S4 & 0xFFFFFFFF
    LFSR_S5 = LFSR_S5 & 0xFFFFFFFF
    LFSR_S6 = LFSR_S6 & 0xFFFFFFFF
    LFSR_S7 = LFSR_S7 & 0xFFFFFFFF
    LFSR_S8 = LFSR_S8 & 0xFFFFFFFF
    LFSR_S9 = LFSR_S9 & 0xFFFFFFFF
    LFSR_S10 = LFSR_S10 & 0xFFFFFFFF
    LFSR_S11 = LFSR_S11 & 0xFFFFFFFF
    LFSR_S12 = LFSR_S12 & 0xFFFFFFFF
    LFSR_S13 = LFSR_S13 & 0xFFFFFFFF
    LFSR_S14 = LFSR_S14 & 0xFFFFFFFF
    LFSR_S15 = LFSR_S15 & 0xFFFFFFFF

    # /* the initialisation procedure of LFSR in the mode of initialization */
    # /* the initialisation procedure of LFSR in the mode of work */
    # /* the initialisation procedure of BRC_Xi */
    # /* the initialisation procedure of F_R1 and F_R2 */
    # /* the initialisation procedure of F_R1
    F_R1 = 0
    F_R2 = 0
    nCount = 32
    while nCount > 0:
        BitReorganization()
        w = F()
        LFSRWithInitialisationMode(w >> 1)
        nCount -= 1


def GenerateKeystream(pKeystream, KeystreamLen):

    # TODO
    BitReorganization()
    F()
    LFSRWithWorkMode()
    # print(BRC_X3)
    for i in range(KeystreamLen):
        BitReorganization()
        # print(BRC_X3)
        pKeystream[i] = F() ^ BRC_X3
        # print(pKeystream[i])
        LFSRWithWorkMode()


def ZUC(k, iv, ks, length):

    # Call the Initialization function to set up the initial state
    Initialization(k, iv)

    # Generate the keystream using the GenerateKeystream function
    GenerateKeystream(ks, length)


def test1():
    IV = [0x00] * 16
    k = [0x00] * 16
    Len = 2
    z = [0x00] * Len

    ZUC(k, IV, z, Len)
    print("{:08x}, {:08x}".format(z[0], z[1]))


def test2():
    IV = [0xFF] * 16
    k = [0xFF] * 16
    Len = 2
    z = [0x00] * Len

    ZUC(k, IV, z, Len)
    print("{:08x}, {:08x}".format(z[0], z[1]))


if __name__ == "__main__":
    test1()
    test2()
