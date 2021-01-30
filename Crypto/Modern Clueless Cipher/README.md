
# Modern Clueless Cipher

Difficulty Level: Medium
After learning basic crypto cipher, I have encrypted the flag and provided you with the key as well. Decrypt it to get the flag.


### Hints

- XOR Encryption
- Look for obfuscation where there could be junk characters


## Deployment

Upload flag.txt in distrib to static file server.

- flag.txt
    - SHA1: 
    - Text file containing encrypted strings


## Solution

This was just an repeating key XOR encryption but with a catch where 'f' is just obfuscation, repeating every three characters in the flag. We remove the Fs and use XOR to solve the challenge. Solution can be found in /solution/solution.py

### Flag
`19C4{repeated_key_xor}`
