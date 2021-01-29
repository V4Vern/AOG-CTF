
# Optical_Character

Difficulty Level: Hard

My friend Tesserect sent me many pictures containing weird characters and I could not seem to figure out what is the flag?

### Hints

- Optical character recognition   


## Deployment

Upload files in the distrib folder to the static file server

- flag1.jpg
    - SHA1: 4846DB74A535ACA244FF1BA9A8657CC35F0FF094
- flag2.jpg
    - SHA1: 539466B0EA303D5C9D71C58FD955B5DF1C5F8404
- flag3.jpg
    - SHA1: D2ECA46EECCFE347DAEA003A664EDF1E84B72889
- flag4.jpg
    - SHA1: 91BBA6EB031C1E53482405B03C7A4B05595D00D0
- flag5.jpg
    - SHA1: 5EFAAA2EDDB6689FF47F9768D998BF8B5AF80E98



## Solution

All images show lines of hexadecimal strings, we can use OCR to extract the text from the image.

The important image is in flag4.jpg. Afterwards, we can decode the hexadecimal strings to ASCII. 

The decoded text seems like it has been rotated, performing a ROT-13 on line 32 will result in the flag. 

### Flag
`19C4{Opt1ca!_ch@r@cter_recognition}`
