from math import gcd


# Finding modular inverse
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# From flag.txt, we have the cipher_text(c),public key(e), product of prime factorisation(n).
# To decrypt the (c), we need to get private key(d)

e = 65537
c = 8206569783334937671777037415577201404218289579161341932805668081037129250420790885971649470621233296860597553868062709510960842882424031568059321540444201481195846790420394482978911744460204322280946897121369569884183537507538043
n = 25217504705091327923619967258555558119954392409205403145472230327043451917476126598007137926101153343505134281980451910548993692600372974764947840497514641293355376605835961472754281773766335786262650066957605665435087046309937021

# We are given `n` which we can perform prime factorisation in order to find `p` and `q`. To do that simply head down
# to [factordb](http://factordb.com/)

p = 3725388540036591041643678991347701532937995068972047889459827083352416094739748803290082375874981227998371945676111
q = 6769093863386297883488638026341328618874310635474126545969024032791150452455022144768609227282398126000693285501811
phi = (p - 1) * (q - 1)

# d * e mod phi = 1
# Afterwards, we can calculate `d` by performing a modular inverse function using the given `e` and `phi`
d = modinv(e, phi)

# We can decrypt the ciphertext `c` using `n` and `d`.
# Get plaintext in integer format
plaintext = pow(c, d, n)
# Convert the integer to bytes, then to a string
flag = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='big').decode('ascii')
print(flag)