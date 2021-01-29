
# Socket

Difficulty Level: Medium

Socket programming? It's very simple, all you need to do is connect and send 32 bytes of the carriage return to the server.

Connect to the server via : 
`nc challenge.ctf-fun.xyz 13000`


### Hints

- Look at the ASCII table for carriage return.


## Deployment

Run sudo ‘./service/build.sh’ 


## Solution

Craft message such as `msg = '\x0D'*32`.We can make use of python encode method and socket programming to send the message to the server and get the flag.

### Flag
`19C4{cl13n7_53rv3r_c0mmun1c4710n}`
