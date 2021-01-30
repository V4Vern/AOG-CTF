
# Weird File

Difficulty Level: Warmup

Hmm for some weird reason I can't open this file? Any ideas ? 

### Hints

- https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5#
- In order to identify a correct file type, we might need to verify the file magic number
- https://www.garykessler.net/library/file_sigs.html



## Deployment

Upload file.docx in the distrib folder to the static file server.

- file.docx
    - SHA1: 7c2a5923ca65b68d2b8fd942a63d5390483c8b7c
    - PNG File


## Solution

By performing hexdump -c secret_1.xtr, one will draw clues that the file begins with an FF D8 and ends with an FF D9 chunk. This could mean the file was originally a jpeg file instead of a docx file

Simply rename the file extension of the docx file to jpeg file, an image will appear and the flag is shown.


### Flag
`19C4{cOrr5ct_fl1e_Ext3nsion}`
