
# Ass-key

Difficulty Level: Warmup
When a computer sends data via the keys you press or the text you send and receive is sent as a bunch of numbers. These numbers represent the characters you typed or generated. Because the range of standard ASS-KEE is 0 to 127 it only requires 7 bits or 1 byte of data. For example to send the string cactus.io as ass-kee it would translate to 99 97 99 116 117 115 46 105 111. Microprocessors only understand bits, bytes & fetch decode executes. 
Using the below integer array, convert the numbers to their corresponding ASS-kee characters to obtain a flag.
[49,57,67,52,123,65,83,83,45,75,69,89,95,73,83,95,65,83,67,73,73,125]


### Hints

- http://www.asciitable.com/

## Deployment

No Deployment are needed

## Solution

ASCII codes can be decoded via an ASCII table which can be found “http://www.asciitable.com/” or it can be decoded using an online decoder in cyber chef or even decoded using python. 

### Flag
`19C4{ASS-KEY_IS_ASCII}`
