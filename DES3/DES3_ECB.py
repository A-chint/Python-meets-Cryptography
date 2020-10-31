from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(24)
t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")

crypto_object = DES3.new(key,DES3.MODE_ECB) 

ct = crypto_object.encrypt(pad(t,DES3.block_size))

print("The encrypted using ECB mode is : ",ct)

pt = unpad(crypto_object.decrypt(ct),DES3.block_size)

print("The plain text using ECB mode is : " ,pt)
