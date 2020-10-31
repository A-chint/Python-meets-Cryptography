from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

key = b"12345678"
t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
init_vector = get_random_bytes(8)

encrypt_object = DES.new(key,DES.MODE_CFB,iv=init_vector)

ct = encrypt_object.encrypt(pad(t,DES.block_size))

print("The encrypted text using CFB mode : ",ct)

decrypt_object = DES.new(key,DES.MODE_CFB,iv=init_vector)

pt = unpad(decrypt_object.decrypt(ct),DES.block_size)

print("The decrypted text using CFB mode : ",pt)
