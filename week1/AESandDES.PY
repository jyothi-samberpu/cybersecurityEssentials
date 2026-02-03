from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

def aes_encrypt(plain_text, key):
    key = key.ljust(16)[:16].encode()  # Ensure key is 16 bytes
    iv = os.urandom(16)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()

def aes_decrypt(encrypted_text, key):
    key = key.ljust(16)[:16].encode()  # Ensure key is 16 bytes
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:16]  # Extract IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted_bytes.decode()

# Test AES
key = "mysecretpassword"
plain_text = "Hello, AES Encryption!"
encrypted_text = aes_encrypt(plain_text, key)
decrypted_text = aes_decrypt(encrypted_text, key)

print(f"AES Encrypted: {encrypted_text}")
print(f"AES Decrypted: {decrypted_text}")




#DES PROGRAM:

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64
import os

def des_encrypt(plain_text, key):
    key = key.ljust(8)[:8].encode()  # Ensure key is 8 bytes
    iv = os.urandom(8)  # Generate a random IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()

def des_decrypt(encrypted_text, key):
    key = key.ljust(8)[:8].encode()  # Ensure key is 8 bytes
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:8]  # Extract IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_data[8:]), DES.block_size)
    return decrypted_bytes.decode()

# Test DES
key = "mypassword"
plain_text = "Hello, DES Encryption!"
encrypted_text = des_encrypt(plain_text, key)
decrypted_text = des_decrypt(encrypted_text, key)

print(f"DES Encrypted: {encrypted_text}")
print(f"DES Decrypted: {decrypted_text}")

