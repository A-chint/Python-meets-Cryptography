from chacha20poly1305 import ChaCha20Poly1305
from Crypto.Random import get_random_bytes

t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
key = get_random_bytes(32)

encrypt_object = ChaCha20Poly1305(key)

nonce = get_random_bytes(12)
ct = encrypt_object.encrypt(nonce,t)
print("Encrypted text is : ",ct)

pt = encrypt_object.decrypt(nonce,ct)
print("Decrypted text is : ",pt)
