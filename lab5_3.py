def vigenere_encrypt(plaintext, key, alphabet):
    # Convert the alphabet into a dictionary with numerical positions
    alphabet_dict = {letter: index for index, letter in enumerate(alphabet)}
    alphabet_len = len(alphabet)

    # Extend the key to match the length of the plaintext
    extended_key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]

    # Encrypt the plaintext
    ciphertext = []
    for p_letter, k_letter in zip(plaintext, extended_key):
        p_index = alphabet_dict[p_letter]
        k_index = alphabet_dict[k_letter]
        c_index = (p_index + k_index) % alphabet_len
        ciphertext.append(alphabet[c_index])

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key, alphabet):
    # Convert the alphabet into a dictionary with numerical positions
    alphabet_dict = {letter: index for index, letter in enumerate(alphabet)}
    alphabet_len = len(alphabet)

    # Extend the key to match the length of the ciphertext
    extended_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]

    # Decrypt the ciphertext
    plaintext = []
    for c_letter, k_letter in zip(ciphertext, extended_key):
        c_index = alphabet_dict[c_letter]
        k_index = alphabet_dict[k_letter]
        p_index = (c_index - k_index) % alphabet_len
        plaintext.append(alphabet[p_index])

    return ''.join(plaintext)

# Ukrainian alphabet
ukrainian_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

# Given plaintext and key
plaintext = 'криптографічніметодизахистуінформації'
key = 'гук'

# Encrypt the plaintext using the Vigenère cipher
ciphertext = vigenere_encrypt(plaintext, key, ukrainian_alphabet)
print('Ciphertext:', ciphertext)

# Decrypt the ciphertext using the Vigenère cipher
deciphered_text = vigenere_decrypt(ciphertext, key, ukrainian_alphabet)
print('Deciphered Text:', deciphered_text)
