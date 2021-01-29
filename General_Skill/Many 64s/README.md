
# Many 64s

Difficulty Level: Hard

Help! My friend did something to my computer when I was away and I didn’t have the time to hide my flag. By the time he gave it back to me, my flag was changed. Can you help me decrypt it?

### Hints

- You might need to do some simple scripting on this 
- https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/



## Deployment

Upload cipher.txt in distrib to static file server.

- cipher.txt
    - SHA1: 1709a4085d1ee6def3776757b5c3e8d31cfd9104
    - Text file containing encrypted strings


## Solution

This file contains 50 times of base64 encoding and you would need to write a script to decode it. Sample solution can be found in ./solution. 

### Flag
`19C4{L00p-Base64}`
