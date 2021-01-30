
# Easter Egg

Difficulty Level: Hard

There is a flag hidden within this image. Can you find it? 

### Hints

-  No hints are needed.



## Deployment

Upload skyscraper.jpg in the distrib folder to the static file server

- skyscraper.jpg
    - SHA1: e900ac7ec6667fff2915e530a61e28341b6c55ea
	
## Solution

Upon opening the image in HxD and noticed that there was a string of Hexspeak for the phrase “DEAD BEEF” at the ending of the image.

Notice that after the JPEG trailer FF D9, it has a starting bit of 00 and prior to the start of DEADBEEF, it also has an ending bit of 00. 

To find for information on this image, I went to my Kali VM and used the strings command on the file:

I then use this website https://onlinehextools.com/xor-hex-numbers to xor the 2 hex strings that I have retrieved:

Navigating to cyberchef to decode the xored hex and it gives me 2 strings “stegception and weakness”.

I assumed that this was the key to extract data from the image thus the first tool I thought of that required a password to extract data from the image was Steghide. Thus, I navigated to an online steghide decoder “https://futureboy.us/stegano/decinput.html” to retrieve the secret output

After viewing the raw output, I can see the file header which was PK and this tells me that it is a zip file. Afterwards, I chose the 3rd option to save the payload instead. 

Upon unzipping the payload file, it requires a password and I uses the other string which was used “stegception” to unzip it. 

Upon unzipping the file, we are able to retrieve a flag.txt but it is in hex which we can decode it in cyberchef

Upon decoding it with hex and base85, we can see the flag as shown below

### Flag
`19C4{the_matryoshka_challenge}`
