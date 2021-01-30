
# Treasure Hunt

Difficulty Level: Easy

The flag is hidden somewhere and it feels like finding a needle in a haystack. 
	
### Hints

- https://en.wikipedia.org/wiki/Steganography



## Deployment

Upload treasure_hunt.jpg in the distrib folder to the static file server 
Run ./generate/built.py to generate treasure_hunt.txt

- treasure_hunt.jpg
    - SHA1: c01e6053000f349fbe355a4919384c4b0f4c57bb
    - JPG File


## Solution

Open the image and scan the QR code at the bottom-right hand corner.

Convert the given decimal characters 109 111 117 115 101 into a valid ASCII text mouse.

Use https://futureboy.us/stegano/decinput.html to extract the hidden text file with the password mouse.

Open up the file and the flag will be hidden amongst a bunch of other junk strings.


### Flag
`19C4{Look_Carefully}`
