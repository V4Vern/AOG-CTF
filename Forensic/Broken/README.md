
# Broken

Difficulty Level: Easy

My Agency employs a method to transfer sensitive documents to prevent other people from seeing it. It does not seem to be opening with that weird file extension. Find out the method and get the flag.  

### Hints

- Sometimes files header can be modified easily to different extensions.
- https://www.garykessler.net/library/file_sigs.html
- Hex Editor is useful :)
- https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5#




## Deployment

Upload secret.xtr in the distrib folder to the static file server.

- secret.xtr
    - SHA1: 7c2a5923ca65b68d2b8fd942a63d5390483c8b7c
    - PNG File


## Solution

By performing hexdump -c secret_1.xtr, one will draw clues that the file begins with an IHDR and ends with an IEND chunk. This could mean the file was originally a PNG file and was corrupted. 

To change the file header from XTR to PNG, open the file in WinHex and edit the first four bytes from 89 58 54 52 to 89 50 4e 47.

An image will appear and the flag is at the bottom-left.

### Flag
`19C4{File_Carving}`
