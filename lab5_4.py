import random
from sympy import isprime

# Function to generate a random prime number of given bit length
def generate_prime(bit_length=8):
    while True:
        num = random.getrandbits(bit_length)
        if isprime(num):
            return num

# Function to calculate the Greatest Common Divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi

# Function to generate public and private keys
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Function to encrypt a message using the public key
def encrypt(public_key, plaintext):
    e, n = public_key
    return pow(plaintext, e, n)

# Function to decrypt a message using the private key
def decrypt(private_key, ciphertext):
    d, n = private_key
    return pow(ciphertext, d, n)

# Main function to demonstrate encryption and decryption
def main():
    public_key, private_key = generate_keys()
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")

    plaintext = 100
    print(f"\nOriginal message: {plaintext}")

    ciphertext = encrypt(public_key, plaintext)
    print(f"Encrypted message: {ciphertext}")

    decrypted_message = decrypt(private_key, ciphertext)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
