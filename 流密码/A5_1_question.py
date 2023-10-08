# 三个移位寄存器的掩码
R1MASK = 0x07FFFF  # 19 bits, numbered 0..18
R2MASK = 0x3FFFFF  # 22 bits, numbered 0..21
R3MASK = 0x7FFFFF  # 23 bits, numbered 0..22

# 三个移位寄存器的中间比特，用于驱动控制
R1MID = 0x000100  # bit 8
R2MID = 0x000400  # bit 10
R3MID = 0x000400  # bit 10

# 反馈插头， 用于对移位寄存器进行驱动
# TODO
R1TAPS = 0x072000  # bits 18,17,16,13
R2TAPS = 0x300000  # bits 21,20
R3TAPS = 0x700080  # bits 22,21,20,7

# 输出插头， 用于输出的生成
R1OUT = 0x040000  # bit 18 (the high bit)
R2OUT = 0x200000  # bit 21 (the high bit)
R3OUT = 0x400000  # bit 22 (the high bit)

# 计算32位比特字的奇偶性，即比特数mod2
def parity(x):
    # TODO
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

# 对移位寄存器进行一次驱动
def clockone(reg, mask, taps):
    # TODO
    t = reg & taps
    reg = (reg << 1) & mask
    reg |= parity(t)
    return reg

# 钟控模块，输出多数比特
def majority():
    # TODO
    sum = parity(R1 & R1MID) + parity(R2 & R2MID) + parity(R3 & R3MID)
    if sum >= 2:
        return 1
    else:
        return 0

# 根据钟控驱动一次
def clock():
    # 把三个寄存器定义为全局变量
    global R1, R2, R3  
    # TODO
    maj = majority()
    if parity(R1 & R1MID) == maj:
        R1 = clockone(R1, R1MASK, R1TAPS)
    if parity(R2 & R2MID) == maj:
        R2 = clockone(R2, R2MASK, R2TAPS)
    if parity(R3 & R3MID) == maj:
        R3 = clockone(R3, R3MASK, R3TAPS)
# 驱动三个寄存器
def clockallthree():
    global R1, R2, R3
    # TODO
    R1 = clockone(R1, R1MASK, R1TAPS)
    R2 = clockone(R2, R2MASK, R2TAPS)
    R3 = clockone(R3, R3MASK, R3TAPS)
# 获取输出比特
def getbit():
    return parity(R1 & R1OUT) ^ parity(R2 & R2OUT) ^ parity(R3 & R3OUT)

def keysetup(key, frame):
    global R1, R2, R3
    R1 = R2 = R3 = 0

    # 装填密钥
    for i in range(64):
        clockallthree()
        # 对字节操作
        # TODO
        R1 ^= ((key[i // 8] >> (i % 8)) & 1)
        R2 ^= ((key[i // 8] >> (i % 8)) & 1)
        R3 ^= ((key[i // 8] >> (i % 8)) & 1)
    # 处理帧号
    for i in range(22):
        clockallthree()
        # TODO
        R1 ^= ((frame >> i) & 1)
        R2 ^= ((frame >> i) & 1)
        R3 ^= ((frame >> i) & 1)
    for i in range(100):
        clock()

def run():
    # 114比特
    AtoBkeystream = bytearray(15)
    BtoAkeystream = bytearray(15)

    for i in range(114):
        clock()
        AtoBkeystream[i // 8] |= getbit() << (7 - (i % 8))

    for i in range(114):
        clock()
        BtoAkeystream[i // 8] |= getbit() << (7 - (i % 8))

    return AtoBkeystream, BtoAkeystream

# 字符串转十六进制
def str_to_hex(hex_str):
    return int(hex_str, 16)

# 测试向量验证
# key: 0x1223456789ABCDEF
# frame number: 0x000134
# A->B: 0x534EAA582FE8151AB6E1855A728C00  
# B->A: 0x24FD35A35D5FB6526D32F906DF1AC0
def test(hex_key, hex_frame):
    # 密钥转为字节
    key = bytearray.fromhex(hex_key)
    # 十六进制转化
    frame = str_to_hex(hex_frame)

    # 密钥初始化
    keysetup(key, frame)
    AtoB, BtoA = run()

    print(f"key: {key.hex().upper()}")
    print(f"frame number: {frame:06X}")
    print("observed output:")
    print(f"A->B: {AtoB.hex().upper()}\nB->A: {BtoA.hex().upper()}")

if __name__ == "__main__":
    
    # 十六进制
    test_key = "1223456789ABCDEF"
    test_frame = "134"
    test(test_key, test_frame)
   
