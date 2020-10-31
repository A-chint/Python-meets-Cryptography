from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad

key = b"12345678"
t = input("Enter the plain text : ")
t = bytes(t,"UTF-8")

crypto_object = DES.new(key,DES.MODE_ECB) 

ct = crypto_object.encrypt(pad(t,DES.block_size))

print("The encrypted using ECB mode is : ",ct)

pt = unpad(crypto_object.decrypt(ct),DES.block_size)

print("The plain text using ECB mode is : " ,pt)
