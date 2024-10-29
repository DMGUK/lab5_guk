
import string
print(string.ascii_uppercase)
alphabet = list(string.ascii_lowercase)

M = "plaintext"

def encrypt(plaintext, key):
    crypto = ""

    for char in plaintext:
        char_index = alphabet.index(char)
        new_char_index = (char_index + key) % 26
        new_char = alphabet[new_char_index]
        crypto += new_char

    return crypto


def decrypt_first_method(crypto, key):
    return encrypt(crypto, -key)

def decrypt_second_method(ciphertext, key):
    plaintext = ""

    for char in ciphertext:
        char_index = alphabet.index(char)
        new_char_index = (char_index - key) % 26
        new_char = alphabet[new_char_index]
        plaintext += new_char

    return plaintext


C = encrypt(M, key=3)
print(C)
M1 = decrypt_first_method(C, key=3)
print(M1)
M2 = decrypt_second_method(C, key=3)
print(M == M1)
print(M == M2)
