
# Spectrum

Difficulty Level: Easy

My friend has been sending me lots of WAV files and I think he is trying to communicate with me.  Find out the message he sent?
	
### Hints

- No hints are needed


## Deployment

Upload listen.me in the distrib folder to the static file server

- listen.me
    - SHA1: 39d8822ca77a1c861b72502026ea11920c7f6124
    - Wav file


## Solution

You have to fix the file header of the wav file and then change it to wav format. 

Download https://www.sonicvisualiser.org/ and open wav file using sonic visualiser.

Under add spectrogram, you can see the flag


### Flag
`19C4{Found_Me}`
