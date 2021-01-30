
# Asymmetric

Difficulty Level: Medium

RSA (Rivest–Shamir–Adleman) is a public-key encryption scheme and is widely used for secure data transmission. Help us decrypt the following message


### Hints

- Look into OpenSSL 


## Deployment

Run ./generate/generate.sh to generate private-key.pem ,public-key.pem & encrypted.rsa

- private-key.pem
    - SHA1: 7227902830d387d93e259094d2c076e893c8ac8f
    - RSA private key
- public-key.pem
    - SHA1: 8917dde941b3b0d1b9b6c60eb6f9ede9b98fad87
    - RSA public key
- encrypted.rsa
    - SHA1:  ebf3a57dc20e330fdae144fcf4777fd361fab42f
    - Encrypted File


## Solution

RSA is an asymmetric cryptographic algorithm, meaning that two different keys are involved in the encryption and decryption process respectively (public key for encryption/private key for decryption). We can decrypt the encrypted file using the private key given :

“ `openssl pkeyutl -decrypt -in encrypted.rsa -inkey private-key.pem` “

We can run in the solution/solution.sh to get the flag as well.


### Flag
`19C4{publ1c_k3y_crypto}'
