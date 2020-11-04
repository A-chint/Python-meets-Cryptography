#////////////////////////DIFFIE-HELMAN KEY EXCHANGE/////////////////////////

p = 23; #publically known value , p is prime
g = 5;  #publically known value , g is primitve root mod of p

print("----------------------------------");
print("Publically known values of p and g");
print("       p = ",p," g = ",g);
print("----------------------------------");

alice_secret_key = 4; #secret key of alice
bob_secret_key = 3; #secret key of bob

print("----------------------------------");
print("   Secret keys of alice and bob   ");
print("       alice = ",alice_secret_key,"   bob = ",bob_secret_key);
print("----------------------------------");

key_shared_by_alice_with_bob = (g**alice_secret_key)%p;

key_shared_by_bob_with_alice = (g**bob_secret_key)%p;

print("----------------------------------");
print("Key shared by Alice : ",key_shared_by_alice_with_bob);
print("Key shared by Bob   : ",key_shared_by_bob_with_alice);
print("----------------------------------");

result_key_with_alice = (key_shared_by_bob_with_alice**alice_secret_key)%p;
result_key_with_bob = (key_shared_by_alice_with_bob**bob_secret_key)%p;

print("----------------------------------");
print("Result key with Alice : ",result_key_with_alice);
print("Result key with Bob   : ",result_key_with_bob);
print("----------------------------------");

