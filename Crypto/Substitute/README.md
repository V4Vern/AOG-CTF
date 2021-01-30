
# Substitute

Difficulty Level: Medium

My Math teacher made me solve this tough math question. I need your help. 

The flag is in the format of 19C4{secret text}. The flag is all lowercase; replace spaces with underscores.


### Hints

- Matrix Multiplication
- A1Z26


## Deployment

Upload homework.txt in distrib to static file server.

- homework.txt
    - SHA1: 
    - Text file containing encrypted strings



## Solution

Multiplying both matrix in the given order string matrix * decoding matrix to get the final product as a 3x7.
[7  4  25 18 15 23 11]
[15 15 15 0  13 15 0 ]
[0  0  21 8  5  18 0]


This is another cipher called Letter Number (A1Z26) Cipher we must again solve.
In this cipher the numbers are substituted with letters, no not ASCII values, just simple A=1;B=2, etc, and solving it from up to down considering 0 as space gives you. Decoding in cyberchef 

https://gchq.github.io/CyberChef/#recipe=A1Z26_Cipher_Decode('Comma')&input=NywxNSw0LDE1LDI1LDE1LDIxLDE4LDgsMTUsMTMsNSwyMywxNSwxOCwxMQ



### Flag
`19C4{go_do_your_homework}`
