import sys
from math import gcd

flag = "19C4{Rsa_is_Fun}"

p = 3725388540036591041643678991347701532937995068972047889459827083352416094739748803290082375874981227998371945676111
q = 6769093863386297883488638026341328618874310635474126545969024032791150452455022144768609227282398126000693285501811
n = p * q  # Prime factorisation
phi = (p - 1) * (q - 1)

e = 65537  # This is the public key
# Check if e is co-prime
if gcd((p - 1), e) != 1 or gcd((q - 1), e) != 1:
    print('Error, e is not a coprime')
    exit()

# Converting flag to bytes, then to an integer
m = int.from_bytes(bytearray(flag, 'ascii'), byteorder='big', signed=False)

c = pow(m, e, n)  # Cipher_text = message ^ e(public key) mod n

with open("flag.txt", "w") as file:
    file.write("e = " + str(e) + "\n")
    file.write("n = " + str(n) + "\n")
    file.write("c = " + str(c) + "\n")