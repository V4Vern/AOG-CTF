
# Interesting_RE

Difficulty Level: Medium

Help me reverse this program and solve the crypto answer.

### Hints

- No hints


## Deployment

Compile the c program: gcc -o rot rot.c   and upload rot in distrib to static file server.

- rot
    - SHA1: 6de129473c14412089c4a6ebe5260c7dede265ad
    - ELF 64-bit LSB executable


## Solution

When looking at the main function, we observe that the program gets user input and strips the trailing new line character. The program then checks if the input has a length of 27 characters, which means that our flag must be 27 characters.
If the input is 27 characters another function called xor is called,which basically performs a XOR bitwise operation between the user input and an array of bytes.After XOR operation has been performed, the input values are compared with an array of bytes. If the two arrays are equal, this will indicate that we have the right flag. 
Hence, to obtain the flag we can XOR the array of bytes in the XOR function and the other array of bytes the program uses to compare the user input



### Flag
`19C4{r0x4nn3_x0r_r0ck_54nd}`
