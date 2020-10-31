from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
init_vector = get_random_bytes(8)
key = get_random_bytes(24)

encrypt_object = DES3.new(key,DES3.MODE_OFB,iv=init_vector)

ct = encrypt_object.encrypt(pad(t,DES3.block_size))

print("Encrypted text using OFB mode is : ",ct)

decrypt_object = DES3.new(key,DES3.MODE_OFB,iv=init_vector)

pt = unpad(decrypt_object.decrypt(ct),DES3.block_size)

print("The decrypted text using OFB mode is : ",pt)
