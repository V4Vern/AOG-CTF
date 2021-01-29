
# .-.-.- .-.-.- .-.-.- 

Difficulty Level: Hard

This is an easy crypto but tricky! ylluferac kooL

### Hints

- Remember hex encoding but look carefully :)
- This is a helpful tool https://onlinehextools.com/reverse-hex-digits



## Deployment

Upload ascii.txt in distrib to static file server. 

- ascii.txt
    - SHA1: 9141f15d0ad13442447d29631c4139b7e1f40518
    - Ascii text


## Solution

We are given with 4c 69 30 74 4c 53 30 67 4c 53 30 74 4c 53 34 67 4c 53 34 74 4c 69 41 75 4c 69 34 75 4c 53 41 67 4c 53 30 67 4c 53 30 74 4c 53 30 67 4c 69 30 75 49 43 34 75 4c 69 30 75 4c 69 30 67 4c 69 41 75 4c 69 30 74 4c 69 30 67 4c 53 34 74 4c 69 41 74 4c 53 30 74 4c 53 41 74 4c 69 34 67 4c 69 41 3d

We will need to use https://onlinehextools.com/reverse-hex-digits for some parts in order to obtain the solution above. It looks like a hexadecimal format. Converting it to ASCII gives a base64 format.

Converting to base 64 gives you “- . ... - ..--.- -.-. - ..-.  -- ----- .- -.-. ----- -.. . “ where you have to convert it from morse code.

Convert it from morse code gives you the flag


### Flag
`19C4{M0R$E_C0DE}`
