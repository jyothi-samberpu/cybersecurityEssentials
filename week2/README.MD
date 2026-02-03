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

Public Key: -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvKstWfcDIMKsvv3cCFxg
m7O9xbjCES4Pc8U/CVa5dWMmdveCRrRbino++VTESClIlNulXF03q+jE0Qer236d
PaPqe4XNva2L8xz+vka85OYlrLprAl6y9vZp4Pl/o2WohAAsZO2ETd4cSP680Heb
eM+GT+bwxLTsLX0q3t/sHd512fDYaeiHWF8vVCWEGA819t0spg/Qifp4MQUVGHp6
deCu367T81vsH0QWnzFKegcMUjov4IRvYsziLEi7VHdjzZnPqDnk8BCVAqPgcMnW
4hjmVrXbn/8MpqvKubJNd80CglTysMG7uItrhJ97sDHDCRzQ9nP4eh+W+MJpxVaL
1wIDAQAB
-----END PUBLIC KEY-----

Private Key: -----BEGIN RSA PRIVATE KEY-----
MIIEoAIBAAKCAQEAvKstWfcDIMKsvv3cCFxgm7O9xbjCES4Pc8U/CVa5dWMmdveC
RrRbino++VTESClIlNulXF03q+jE0Qer236dPaPqe4XNva2L8xz+vka85OYlrLpr
Al6y9vZp4Pl/o2WohAAsZO2ETd4cSP680HebeM+GT+bwxLTsLX0q3t/sHd512fDY
aeiHWF8vVCWEGA819t0spg/Qifp4MQUVGHp6deCu367T81vsH0QWnzFKegcMUjov
4IRvYsziLEi7VHdjzZnPqDnk8BCVAqPgcMnW4hjmVrXbn/8MpqvKubJNd80CglTy
sMG7uItrhJ97sDHDCRzQ9nP4eh+W+MJpxVaL1wIDAQABAoIBACrWMtXaX7tweAhl
WzAKyWSQyuW5rVZ5PsjqYAWeyzz75h/c0pd7G821M9coh+had0BVHpZ6E8nUb9uG
Al8zwD/el760AqKuZLguPSi2puzR1HwDV4iSN9Aa4q9R9skCq+BMqcfApemIJKPu
MrCid4pWlAhQRxpieb1aTgGMle+xzqXa3JHbUWgnllhuZ1fxLymKMbt6RfsGnT3o
PsWMxBqBlVw1i0OP7CRzbIeWiwhiWh4dHJUG2hoVfhE1aCGB4OtvPYci3aN0qucT
qlD62UuUtl9YRl7RPx44M1GTHwC4DVMpeol5R5Oq1kCkvWaSbGQzwgCHb9O2AUDb
yPB3aAECgYEAybNW9onNqpoliHNXFdW546XpKzOLxOnapiS/4OowFt/zkWAB41Id
/0yi0NN4XRvzmOQsDosGSkeZuXL1NIy6hsoUN6Gar0YkzEiLiXxRMw7Fdj8YA2ap
bfMNqBQ0zcJCv5+NDAgA2DJlvFPLyH3Ub8Wsau2RWS9zIMdTv/YXUOECgYEA73W3
BOQZJ45y7v+OBYw73+UpfTiAt5PLuKU5sx4gYc8VlQDdQjpfycnULjVfa3WE0ZBW
5HZ3Rzk2C/sORfkdKmkX4famSNLleyyhrMJIkP8gwToMZ4RaD0u3KIjAYRaWrpkq
wxlF01XvAqzIuQ7bn2Yez/B/y2sOGMJGTjWkG7cCgYBNL0LND0jTyy8nuzONGH+N
HPVQYeZPkUnpoFCJCjUi28qCTCIM0mTGSJZZoUMDJmoejNpLKmpazHGIJPSuilfq
srPv4fimsAnu3qf/EcKk7jckG9rdmlCl0YfdVPYr8vXGDJFWFE32bbq+ybZG39gG
ebeUJ5sibOT6myxyXgLoIQKBgBHB7PyT3bmtOqC2mtWWfKox2E3M7t6uOyFKP2kl
Bsm6DaOrGL1cjtXr/awfkR/q6xqPVaJDlrzVZUimKXzO6HbIrFi5bcNgwFvOB39E
ORVnlgo+P8U9b2BLAR4kZf/NKQdxnFYzfZYafUr5fTkb/PVpIUfSUefH3JfBcG1E
VRMpAn8mVd2iz5wLEzEvsDmzT4Nv7yqYphp+LspKXmM/K2pa6uSg3DIt2uGCtJzq
czeRbsbIgL96U4mpP2eOEV+PpKWfI1T5Fiycy/jCLtxDl8i67FYmHEzsScskJ2KN
BEUBcApiQTLPPYolXr0Mw3MYamklGhZlG5Iw7j8e7WcxvpkM
-----END RSA PRIVATE KEY-----

Original Message: Hello, RSA Encryption!
Encrypted Message: IBvQBsvI0Dy8rqqJSB9gh+DCRmDHErCjIXKEUUBWdxmjbxp+JYTfFAeIOqIv8LboZNa4XqUpgvY43CdiPUC61p1MitUXDIRzHB0ituSyvoDPW2uUZAm+ci2FXSmZSUot1zV1e5QBy3HcGU2+EuNIQlyHzUmI5o8EaXbHegNqwEY72oZlpKifrFmB2u4GtRiwskoz6eze9sCKYmAibv+ZAi2oeBMUEiNcYSBVk4WFUMBtVv1oG/vEAj9tiZaq8vK20GziBXyEmtPyO32b0vcSFxfN20OOR7m96lX1Vifl26vV8O1kP4JA2dyOVjCNoIBGXeKe1JqUI3Yt4a+58O2yXg==
Decrypted Message: Hello, RSA Encryption!
