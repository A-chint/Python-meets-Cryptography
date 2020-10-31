from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(24)
t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
init_vector = get_random_bytes(16)

encrypt_object = AES.new(key,AES.MODE_CBC,iv=init_vector)

ct = encrypt_object.encrypt(pad(t,AES.block_size))

print("Encrypted text using CBC is : ",ct)

decrypt_object = AES.new(key,AES.MODE_CBC,iv=init_vector)

pt = unpad(decrypt_object.decrypt(ct),AES.block_size)

print("The Decrypted test using CBC mode is : ",pt)
