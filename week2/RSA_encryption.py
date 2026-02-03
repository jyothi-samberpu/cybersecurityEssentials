from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA Key Pair
def generate_keys():
    key = RSA.generate(2048)  # 2048-bit key size
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt message using the public key
def rsa_encrypt(message, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher_rsa.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()

# Decrypt message using the private key
def rsa_decrypt(encrypted_message, private_key):
    private_key_obj = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key_obj)
    decrypted_message = cipher_rsa.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode()

# Test RSA Encryption and Decryption
private_key, public_key = generate_keys()
print("Public Key:", public_key.decode())  # Sharing allowed
print("\nPrivate Key:", private_key.decode())  # Keep secret

message = "Hello, RSA Encryption!"
encrypted_msg = rsa_encrypt(message, public_key)
decrypted_msg = rsa_decrypt(encrypted_msg, private_key)

print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted_msg)
print("Decrypted Message:", decrypted_msg)
