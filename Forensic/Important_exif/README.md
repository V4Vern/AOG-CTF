
# Important_exif

Difficulty Level: Warmup

EXIF is the key to finding this flag.

### Hints

- No hints are provided



## Deployment

Upload Important_Document.pdf in the distrib folder to the static file server.

- Important_Document.docx
    - SHA1: 
    - PNG File


## Solution

There appears to be a hidden zip file inside the original pdf file. We can use the tool “foremost” or “binwalk” to extract the hidden zip file. 

The other alternative would be using the binwalk tool which is available in kali linux via this command “binwalk --dd='.*' file.jpg”. It will auto extract out the hidden file which is the zip file.

The zip file is password protected and the password can be found via examining the exif of the original pdf file which the password is “ctf_is_fun”. Upon extracting the  zip file, it contains a text file which contains the flag

### Flag
`19C4{EXIF_EXIT}`
