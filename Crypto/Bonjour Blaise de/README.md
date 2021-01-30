
# Bonjour Blaise de

Difficulty Level: Easy

John walked to the doorsteps of his house, he saw a letter with a title “le chiffre indéchiffrable” on the floor. 

You are required to obtain the secret key and put it into the 19C4 flag format, i.e. 19C4{key}.

### Hints

- This is a ciphertext-only (COA) attack where you need to brute force the secret key.

## Deployment

Upload cipher.txt in distrib to static file server.

- cipher.txt
    - SHA1: 918c9b83104343c67e1c40694b37490194013926
    - Text file containing encrypted strings


## Solution

1.	The phrase ‘le chiffre indéchiffrable’ in the challenge statement suggests that the characters have been encrypted using a vigenère cipher.
2.	With Guballa Vigènere Solver at https://www.guballa.de/vigenere-solver, paste the ciphertext and attempt to break the cipher with the following configurations.
     - Cipher Variant: Classical Vigènere
	 - Language: English
	 - 3-30

### Flag
`19C4{vigenere_weak}`
