from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
key = b"12345678"
nonc = get_random_bytes(4)
iv = get_random_bytes(4)

encrypt_object = DES.new(key,DES.MODE_CTR,nonce=nonc,initial_value=iv)
#counter = nonce + initial_value

ct = encrypt_object.encrypt(pad(t,DES.block_size))

print("The encrypted text using CTR is : ",ct)

decrypt_object = DES.new(key,DES.MODE_CTR,nonce=nonc,initial_value=iv)

pt = unpad(decrypt_object.decrypt(ct),DES.block_size)

print("The decrypted text using CTR is : ",pt)
