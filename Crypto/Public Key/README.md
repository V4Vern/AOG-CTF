
# Public_Key 

Difficulty Level: Hard

After learning more about RSA, I decided to play and experiment with its encryption method. Decrypt the message using those variables that I have kindly provided.


### Hints

- Prime factorisation helps


## Deployment

Run ./generate/generate.py to generate flag.txt

- flag.txt
    - SHA1:  857afead814a8cb1e57ebc3bca5662cf57b2d4b6
    - Text file containing e, n and c 


## Solution

We are given n (product of the prime numbers), c (cipher text) and e(public key). To decrypt the ciphertext : 

[C ^ D (Private key)] mod [n]

1.	We are given ‘n’ which we can perform prime factorisation in order to find `p` and `q`.  To do that simply head down to [factordb](http://factordb.com/)
2.	Afterwards, we can calculate phi = (p-1)(q-1)
3.	Afterwards, we can calculate `d` by performing a modular inverse function using the given `e` and `phi`
4.	We can decrypt the ciphertext `c` using `n` and `d`.

The solution can be found in solution/solution.py.

### Flag
`19C4{Rsa_is_Fun}`
