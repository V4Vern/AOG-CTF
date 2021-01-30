
# Hidden File

Difficulty Level: Warmup

There appears to be a hidden file inside this file. Can you help me to extract this file? 

### Hints

- https://www.klennet.com/carver/carving-methods.aspx#:~:text=File%20carving%20is%20a%20process,is%20the%20most%20common%20example.



## Deployment

Upload file.docx in the distrib folder to the static file server.

- file.docx
    - SHA1: 
    - PNG File


## Solution

There appears to be a hidden jpeg file inside the original jpeg file. We can do this manually by extracting out a subsection of a file (FF D8 to FFD9)  and  copy bytes and paste them as a new file. 

The other alternative would be using the binwalk tool which is available in kali linux via this command “binwalk --dd='.*' file.jpg”. It will auto extract out the hidden file which is another jpeg which contains the flag.


### Flag
`19C4{Fi1E_E4tr3ctlon_@re_3ASY}`
