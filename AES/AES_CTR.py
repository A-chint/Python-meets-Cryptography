from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
key = get_random_bytes(24)
nonc = get_random_bytes(8)
iv = get_random_bytes(8)

encrypt_object = AES.new(key,AES.MODE_CTR,nonce=nonc,initial_value=iv)
#counter = nonce + initial_value

ct = encrypt_object.encrypt(pad(t,AES.block_size))

print("The encrypted text using CTR is : ",ct)

decrypt_object = AES.new(key,AES.MODE_CTR,nonce=nonc,initial_value=iv)

pt = unpad(decrypt_object.decrypt(ct),AES.block_size)

print("The decrypted text using CTR is : ",pt)
