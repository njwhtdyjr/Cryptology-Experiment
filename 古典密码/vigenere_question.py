# Title ：维吉尼亚密码 学生填写模板

# 维吉尼亚密码加密函数
def vigenere_encrypt(plaintext, key):
    # 密钥全部大写处理
    key = key.upper()

    cipher = []
    plaintext = plaintext.upper() # 全部大写

    # TODO
    num = len(key)
    shift = []
    i = -1
    for char in key:
        shift.append(ord(char)-ord('A'))
    for char in plaintext:
        i = (i+1)%num
        ascnum = ord(char)
        if ascnum+shift[i]  > ord('Z'):
            ascnum -= 26
        newchar = chr(ascnum + shift[i])
        cipher.append(newchar)

    return ''.join(cipher) # 把列表形式的cipher转化为字符串形式

# 维吉尼亚密码解密函数
def vigenere_decrypt(ciphertext, key):
    # 密钥全部大写处理
    key = key.upper()
    plain = []
    ciphertext = ciphertext.upper()

    # TODO
    num = len(key)
    shift = []
    i = -1
    for char in key:
        shift.append(ord(char) - ord('A'))
    for char in ciphertext:
        i = (i + 1) % num
        ascnum = ord(char)
        if ascnum-shift[i] <ord('A'):
            ascnum += 26
        newchar = chr(ascnum - shift[i])
        plain.append(newchar)

    return ''.join(plain)

plaintext = "hello, world"
# 将明文的其他字符进行去除， 只对英文进行处理
f = filter(str.isalpha, plaintext)
plaintext_strip = "".join(f)

key = "KEY"

# 加密
encrypted_text = vigenere_encrypt(plaintext_strip, key)
print("Plaintext:", plaintext_strip.upper())
print("Encrypted:", encrypted_text)

# 解密
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
