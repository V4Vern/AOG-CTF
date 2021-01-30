
# Disable

Difficulty Level: Warmup

I love to eat pasta but I won’t tell you the secret sauce to it.

Connect at http://web.ctf-fun.xyz:15006


### Hints

- No hints are given.


## Deployment

Run  sudo ./build.sh in service to static file server.


## Solution

This web challenge is a slight variation on the traditional view source challenges. The slight variation being that this challenge includes two very annoying "defense mechanisms" which are disabling right click and disabling ctrl + u.

These "defense mechanisms" can be bypassed by prepending "view-source:" to the start of the URL. Once you view the source, there is nothing obivious on the index.html page. However, if you click on disableMouseRightClick.js, the flag will appear at the bottom of the file.


### Flag
`19C4{n0_k37chup_ju57_54uc3_r4w_54uc3_9873984579843} `
