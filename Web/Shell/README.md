
# C2_Server

Difficulty Level: Hard

I made a new app landing page and I’m currently still working on this feature that allows users to upload images to the website.

Connect at http://web.ctf-fun.xyz:15013/

### Hints

- No hints are provided

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

As mentioned, the user is working on this new feature where we can find it via /uploads where it contains the upload directory. /upload.php contains a webpage where you are able to upload images and it is kind of clear that the challenge is about getting a shell and eventually finding out flag.txt 
You can simply embed a shell inside an image and force the server to connect back to you via a reverse shell. 


### Flag
`19C4{FILE_UPLOAD_ISN'T_SECURE}`
