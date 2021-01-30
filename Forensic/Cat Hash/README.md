
# Cat Hash

Difficulty Level: Medium

We intercepted a hash located in hash.txt, and we believe that the hash belongs to one of the entries in passwords.lst. Help us find the matching pair and you will be rewarded for your efforts.

### Hints

- Identify the hash function used in hash.txt
- https://hashcat.net/hashcat/



## Deployment

Run ./generate/generate.py to generate password.lst
Upload hash.txt in the distrib folder to the static file server

- Song_lyrics 
    - SHA1: 795a804ad99711012ab1517e413d107e11e704b8
    - Text file


## Solution

Identify the hash function used in hash.txt, which is Raw SHA-256

Perform a dictionary attack using lookup.lst as the wordlist:
e.g Using hashcat — hashcat -m 1400 hash.txt passwords.lst


### Flag
`19C4{4ccur4cy!sb5d}`
