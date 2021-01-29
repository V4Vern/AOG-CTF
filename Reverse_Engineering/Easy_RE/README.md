
# Easy_Re

Difficulty Level: Warmup

I am new to C programming so I made a simple program to play with it.

### Hints

- No hints


## Deployment

Compile the c program: gcc -o easy_re generate.c  and upload easy_re in distrib to static file server.

- easy_re
    - SHA1: 8a51dec2c78722241c17a313e8a09934ee8fd794
    - ELF 64-bit LSB executable


## Solution

View the strings of the binary and searching for the flag from the output:

`strings easy_re | grep 19C4`


### Flag
`19C4{57r1n65_4r3_ju57_ch4r4c73r5_1n_4_57r1n6}`
