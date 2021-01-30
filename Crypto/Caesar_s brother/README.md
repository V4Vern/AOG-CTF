
# Caesar’s brother 

Difficulty Level: Warmup

The "Caesar Box," or "Caesar Cipher," is one of the earliest known ciphers. Developed around 100 BC, it was used by Julius Caesar to send secret messages to his generals in the field. In the event that one of his messages got intercepted, his opponent could not read them. However, his form of encryption was weak and his brother decoded a stronger form of encryption. Decode this secret text to get the flag. 

The flag format is in the form of 19C4{secret text}


### Hints

- https://en.wikipedia.org/wiki/ROT13


## Deployment

Upload Secret_Text.txt in distrib to static file server.

- Secret_Text
    - SHA1: c1009a96d674fc8bf81bfa56cfd93a780fb73c65
    - Text file containing encrypted strings


## Solution

Navigate to and paste the cipher to https://www.dcode.fr/rot-47-cipher .

### Flag
`19C4{Weak_Cipher}`
