
# Rot x

Difficulty Level: Hard

Rot 13, Rot 47 are mainstream. Thus, I encrypted the flag using my own Rot x. Decrypt it to get the flag.

### Hints

- ●	Each letter is shifted by x positions


## Deployment

Run ./generate/generate.py to generate challenge.txt

- challenge.txt
    - SHA1:  857afead814a8cb1e57ebc3bca5662cf57b2d4b6
    - Encrypted Text File


## Solution

The title hints at the well known Caesar Shift Cipher. If we try to ROT13 or use substitution cipher solvers on the ciphertext, we don't get any useful results. There are a couple things that we can observe to help us proceed. The first is that the title is called "rot-i". This hints at each element being rotated by a different amount. Punctuation has also been preserved, so we can use this to guess what the plaintext might be. Specifically, the first word looks like it might say "You're" or "You've", and indeed if we look a bit closer, Y = Y + 0, p = o + 1, w = u + 2, and so on... It looks like each letter is shifted by i positions, where i is its index in the message

The solution can be found in solution/solution.py.


### Flag
`19C4{crypto_is_fun_kjqlptzy}`
