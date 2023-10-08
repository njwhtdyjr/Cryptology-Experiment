def initialize_rc4(key):
    # TODO
    # 密钥编排算法
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_encrypt(data, key):
    S = initialize_rc4(key)
    i = j = 0
    result = []
    # TODO
    # 伪随机数生成算法
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(result)

def rc4_decrypt(data, key):
    # RC4 加解密相同
    return rc4_encrypt(data, key)

# 测试向量
# Plaintext: Attack at dawn
# Encrypted: 45a01f645fc35b383552544b9bf5
# Decrypted: Attack at dawn
if __name__ == "__main__":
    # plaintext = b"Plaintext"
    # key = b"Key"
    plaintext = b"Attack at dawn"
    key = b"Secret"

    encrypted_data = rc4_encrypt(plaintext, key)
    decrypted_data = rc4_decrypt(encrypted_data, key)

    print("Plaintext:", plaintext.decode("utf-8"))
    print("Encrypted:", encrypted_data.hex())
    print("Decrypted:", decrypted_data.decode("utf-8"))
