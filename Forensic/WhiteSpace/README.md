
# Whitespace

Difficulty Level: Medium

Christmas is coming !! Santa has sent you some files to take a look. It appears to have something hidden inside the files. 

### Hints

- Tools are available in Google to decrypt whitespaces


## Deployment

Upload Song_lyrics  in the distrib folder to the static file server

- Song_lyrics 
    - SHA1: 68ea11a9197d66aa8a09fa83084752aab582d42f
    - Text file


## Solution

SNOW (Steganography Nature Of Whitespace) is used to hide the flag within the text file.

By using the SNOW tool, the hidden message can be extracted. The Password “christmassss” used for the encryption can be found at the metadata of the image. 

In Linux, the following command can be used to extract the message: “stegsnow -p snowy Song_lyrics.txt”

In Windows, SNOW.exe can be downloaded and the following command can be used to extract the message: “SNOW.EXE -p snowy Song_lyrics.txt”

After extracting the hidden message, you will get the flag 19C4{CHR157MA5_5P1R17}



### Flag
`19C4{CHR157MA5_5P1R17}`
