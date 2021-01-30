
# Parrot

Difficulty Level: Medium

John likes using the Parrot Operating System however, he often gets paranoid and always tries to hide stuff but he often leaves traces of comments around. What is he hiding?

### Hints

- Find comments from the extracted file
- Possible to bruteforce the zip file



## Deployment

Upload parrot.jpg in the distrib folder to the static file server

- Parrot.jpg
    - SHA1: ee030d49cd68a85fb2cec7e326e518a23faea216
	
## Solution

First, use steghide to extract the zip hidden in the parrot.png file with a blank password. If you check the comment in the zip using zipnote, it shows ROCKYOU. This is a hint that you have to use rockyou.txt to bruteforce the password for the zip.

First, we convert the zip to a format readable by John The Ripper using zip2john via the following command :
- zip2john flag.zip > flag

Then use john with rockyou.txt:
- john --wordlist="rockyou.txt" flag

This shows you the password tiagoratix. You get a txt file flag.txt, open it to see the flag.


### Flag
`19C4{1_h0pe_y0u_don't_sEE_m3_here}`
