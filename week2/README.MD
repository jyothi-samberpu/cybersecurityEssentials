2. Implement RSA encryption to demonstrate the concept of public and private keys.

Here’s an example of implementing RSA encryption and decryption in python. This program demonstrates how public and private keys work by using a simple RSA algorithm.

Explanation
Key Generation:

1. Two large prime numbers p and q are chosen.
2. Compute n = p _ q and phi = (p - 1) _ (q - 1).
3. Select a public exponent e such that gcd(e, phi) = 1.
4. Compute the private key d such that (d \* e) % phi = 1.
   Encryption:
5. Use the public key (e, n) to encrypt the message M using the formula: C=Memod  nC = M^e \mod nC=Memodn
   Decryption:
6. Use the private key (d, n) to decrypt the ciphertext C using the formula: M=Cdmod  nM = C^d \mod nM=Cdmodn
   Example Output for Explanation:

CopyEdit
Public Key: (e = 17, n = 3233)
Private Key: (d = 2753, n = 3233)
Plaintext: 42
Ciphertext: 2557
Decrypted text: 42
This is a basic demonstration and should not be used for real-world applications since it lacks security measures and uses small key sizes. For practical purposes, use well-established cryptographic libraries.

# OUTPUT:

Original Message: Hello, RSA Encryption!
Encrypted Message: IBvQBsvI0Dy8rqqJSB9g
Decrypted Message: Hello, RSA Encryption!
