ciphertext = "KHOORZRUOG"

# 穷举26个密钥， 然后对密文进行解密， 并且把结果输出，
# 观察哪个结果是有语义的
def bruteforce(ciphertext):
    # TODO
    for key in range(26):
        decrypted_text = ""
        for char in ciphertext:
            ascnum = ord(char)
            if ascnum-key <ord('A'):
                ascnum += 26
            newchar = chr(ascnum-key)
            decrypted_text += newchar
        print(decrypted_text,' ',key)

bruteforce(ciphertext)
