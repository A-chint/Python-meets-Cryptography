from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")
key = get_random_bytes(24)
nonc = get_random_bytes(4)
iv = get_random_bytes(4)

encrypt_object = DES3.new(key,DES3.MODE_CTR,nonce=nonc,initial_value=iv)
#counter = nonce + initial_value

ct = encrypt_object.encrypt(pad(t,DES3.block_size))

print("The encrypted text using CTR is : ",ct)

decrypt_object = DES3.new(key,DES3.MODE_CTR,nonce=nonc,initial_value=iv)

pt = unpad(decrypt_object.decrypt(ct),DES3.block_size)

print("The decrypted text using CTR is : ",pt)
