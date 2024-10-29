M = "криптографія"

def encrypt(plaintext, key):
    crypto = ""
    for i in range (key, 0, -1):
        text_i = plaintext[i-1::key]
        crypto += text_i
    return crypto


def decrypt(crypto, key):
    return encrypt(crypto, len(crypto) // key)[::-1]

C = encrypt(M, key=3)
print(C)
M1 = decrypt(C, key=3)
print(M1)
print(M == M1)
print()
