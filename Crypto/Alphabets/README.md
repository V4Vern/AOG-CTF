
# Alphabets 

Difficulty Level: Easy

While I was teaching my kids on Alphabets, I was thinking about using an encryption algorithm so I tried to encrypt a message using Alphabets which resulted in the following cipher. Decrypt the following cipher to get the flag.

cipher = "AAAAB AAAAA AAABA ABBAB ABBAA ABAAA BAAAB BAABA AAAAA BAAAB BAABA BABBA "

The flag format is in the form of 19C4{secret text}


### Hints

- Bacon and Shakespeare


## Deployment

- No deployment needed


## Solution

It is clear that the message was encrypted by Bacon's cipher : Bacon's cipher or the Baconian cipher is a method of steganography. To encode a message, each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'. This replacement is a binary encoding and is done according to the alphabet of the Baconian cipher. We can use this online tool for Bacon’s cipher decoder : http://www.dcode.fr/chiffre-bacon-bilitere


### Flag
`19C4{BACONISTASTY}`
