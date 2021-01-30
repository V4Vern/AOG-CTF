
# Many Primes
Difficulty Level: Hard

Using one prime factor seems to be a bad idea  so I'll try using many prime numbers to make it more secure instead.\

### Hints

- No hints are provided


## Deployment

Run ./generate/generate.py to generate flag.txt

- flag.txt
    - SHA1:  
    - Encrypted Text


## Solution

There are many prime numbers after factoring N and these prime numbers can be multiplied together to get the value of PHI. The rest of the method is same as the normal RSA decryption.

The solution can be found in solution/solution.py.

### Flag
`19C4{700_m4ny_5m4ll_f4c70r5}`
