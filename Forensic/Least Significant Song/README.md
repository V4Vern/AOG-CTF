
# Least Significant Song

Difficulty Level: Hard

My friend told me he has made a new song and would want me to have a review on the song. However, he mentioned that there was a secret message hidden in the song and he did mention looking into the song bit-by-bit.

### Hints

-  There is something very significant in the least significant bits.



## Deployment

Upload song.wav in the distrib folder to the static file server

- song.wav
    - SHA1: 769efda3abf900f9e6d596bb6ff9edaa79842282
	
## Solution

1.	The Least Significant Bit (LSB) is a classical method of audio steganography. There is a script that can extract the LSB of each byte and converts the bits into a readable string, which is the flag

### Flag
`19C4{lsb_1s_f0n}`
