
# Communication

Difficulty Level: Medium

My friend invented a way to send messages over without being discovered by the authorities. Decode the message that was sent over.  

### Hints

- Rotation might be needed at some point of time 


## Deployment

Upload music.wav  in the distrib folder to the static file server

- music.wav 
    - SHA1: af272a08370197904f817d1c8f2cfb0132df3972
    - Wav file


## Solution

You have to navigate to https://morsecode.world/international/decoder/audio-decoder-adaptive.html and upload the audio to the site to decode the message.

Upon decryption, there will be a ciphertext which is encoded using base32.

After decryption, you will need to apply an ROT47 rotation to get the flag. 



### Flag
`19C4{Forensic_Is_Interesting}`
