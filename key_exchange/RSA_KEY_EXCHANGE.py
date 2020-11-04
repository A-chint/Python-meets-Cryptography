#////////////////////////RSA KEY EXCHANGE/////////////////////////

p = 17 #publically available value
q = 11 #publically available value

print("-------------------------------------");
print("	value of p : ",p);
print("	value of q : ",q);
print("-------------------------------------");

n = p*q;  
fi = (p-1)*(q-1);  #calculating the value of fi

print("-------------------------------------");
print("	value of fi(n) : ",fi)
print("-------------------------------------");

e = 7; #such that e and funct is coprime , our public key

print("-------------------------------------");
print("value of e : ", e ,"{ aka public key }");
print("-------------------------------------");

k = 0;

def secretExp(fi, e, max=1000):
        k = 1
        while True:
            d = ((fi * k) + 1) / e
            if d.is_integer() is True:
                return int(d)
            k = k + 1
            if k == max:
                return None

d = secretExp(fi,e);

print("-------------------------------------");
print("value of d : ", d ,"{ aka private key }");
print("-------------------------------------");
