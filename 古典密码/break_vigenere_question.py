from math import sqrt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = 'XNPINYOAEMRMRXANRRATBAASEMMBXANRCMZFHBLTMTUVXNLVXMUECMZBAAHGXTRRHDGUJHXDGSYNEQXANMFSPQEAXANYJIKNOYHXWOHKABHRWXWTGLXVOHXBWTBXANWBVEMTBWXNKGLXRRSSKCUAILCHRJBASGPBCTYIIRGJELEEECEJZLLXMIQRMFAAXMXWBVDJTNPEJNQLXKUVPMQIFLHDSRSNCOSWMAAJXANSRGHWDYMMCLRTBPWBVDNDNPBCTYIURTUEKMEEFNCHRATBSBQXFHNXEJZLXHXAAHANBHMECHVWAXUFIHDTBJLCIPOLCHRRMQELWTWGNRWMAAGXMAAHIUALIWCOTIMQEEXANRRWMXFGLXMALXANTUMKMLVXMUECMZFOEOXMHNVWJLYHTHAAHUDIYXARSUSNBEJMMQBEMVTSVXPJSNWMDRQCAXUFIVXMCPXCEJMMQASMGNFVVXYLNGXJNQGARMAIRRTYSHTEQPBTEVXVXUYHPRTUWMJNQXANSGVHWGRWMFIAHLCHRRXGTQERJWBPYQACTXWEQXHYAFWUHTUIEJNRAANRRXANTUVXNLVXMUECMZBLVZXMAAHANSNAMQEFXKJWUSNBENRWQEFQXULRHMQECMZRNFMWNHRXAXUTLMCHRTBPWBYEMMNOXJMVKACYSMGNMREEJNQLBBMBYMQBRKTWTBATCEE'

def decrypt(ciphertext,key):
    plaintext = ''
    for i in range(len(ciphertext)):
        p = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[i%len(key)])
        c = (p - k) % 26
        plaintext += ALPHABET[c]
    return plaintext

# 计算两个序列的向量角度 cosine
def cosangle(x,y):
    numerator = 0
    lengthx2 = 0
    lengthy2 = 0
    for i in range(len(x)):
        numerator += x[i]*y[i]
        lengthx2 += x[i]*x[i]
        lengthy2 += y[i]*y[i]
    return numerator / sqrt(lengthx2*lengthy2)

# 英文单词的频率表
# https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
monofrequencies = [0]*26
monofrequencies[0] = 0.0812
monofrequencies[1] = 0.0149
monofrequencies[2] = 0.0271
monofrequencies[3] = 0.0432
monofrequencies[4] = 0.1202
monofrequencies[5] = 0.0230
monofrequencies[6] = 0.0203
monofrequencies[7] = 0.0592
monofrequencies[8] = 0.0731
monofrequencies[9] = 0.0010
monofrequencies[10] = 0.0069
monofrequencies[11] = 0.0398
monofrequencies[12] = 0.0261
monofrequencies[13] = 0.0695
monofrequencies[14] = 0.0768
monofrequencies[15] = 0.0182
monofrequencies[16] = 0.0011
monofrequencies[17] = 0.0602
monofrequencies[18] = 0.0628
monofrequencies[19] = 0.0910
monofrequencies[20] = 0.0288
monofrequencies[21] = 0.0111
monofrequencies[22] = 0.0209
monofrequencies[23] = 0.0017
monofrequencies[24] = 0.0211
monofrequencies[25] = 0.0007


# 计算重合指数
def index_of_coincidence(text):
    ans = 0

    # TODO

    text = text.upper()

    length = len(text)
    nums = [0]*26
    for char in text:
        nums[ord(char)-ord('A')] += 1
    for i in range(26):
        ans += nums[i]*(nums[i]-1)
    ans /= (length*(length-1))
    return ans

# 由重合指数计算密钥长度
length_of_key = 0
# TODO
n = len(ciphertext)
#min_distance是一个足够大的数
min_distance = 100
for m in range(1,int(n/2)+1):
    distance = 0
    for i in range(m):
        distance += (index_of_coincidence(ciphertext[i::m])-0.065)**2
    distance = sqrt(distance/m)
    if min_distance > distance:
        length_of_key = m
        min_distance = distance

# 输出密钥长度
print(length_of_key)

# 按密钥长度计算各密文切片的频率表
frequencies = []
for i in range(length_of_key):
    frequencies.append([0]*26)
# TODO

ciphertext = ciphertext.upper()
for j in range(length_of_key):
    for char in ciphertext[j::length_of_key]:
        frequencies[j][ord(char) - ord('A')] += 1
    for i in range(26):
        frequencies[j][i] /= len(ciphertext[j::length_of_key])
key = ['A']*length_of_key

# 对每个密文切片， 穷举26个密钥， 计算密文切片使用该密钥移位后的频率分布
# 与英文频率分布序列的余弦值，值越大， 说明与英文频率分布越相似， 最后取
# 余弦值最大的那个密钥作为最终密钥。 
# 注意这个方法需要密文长度较大， 大约需要密文长度是密钥长度的100倍。

for i in range(length_of_key):
    # TODO
    newkey = 0
    cos = -1
    newfrequencies = [0] * 26
    for k in range(26):
        for j in range(26):
            newfrequencies[j] = frequencies[i][(j - k) % 26]

        now_cos = cosangle(newfrequencies, monofrequencies)

        if now_cos > cos:
            cos = now_cos
            newkey = 26 - k
    if newkey == 26:
        newkey = 0
    key[i] = chr(ord('A')+newkey)
print(key)

# 解密
plaintext = decrypt(ciphertext,key)
print(plaintext)
