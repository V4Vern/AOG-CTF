
# Bad_DNS

Difficulty Level: Medium

We launched a game but after the admin resigned 2 days ago, it is no longer launched. Can you figure out what happened?

Connect at http://web.ctf-fun.xyz:15007



### Hints

- -	No hints are given.

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

Challenge starts with a web page which references a down game. Inspecting the source we see a reference https://challenge.ctf-fun.xyz navigating to this website gives us the error DNS_PROBE_FINISHED_NXDOMAIN. This means the DNS server could not find an IP for this address. Let's see if we can find anything else.

Looking for TXT records with

dig challenge.ctf-fun.xyz TXT we get back a TXT file with the flag


### Flag
`19C4{wait_im_confused_what_are_record_types_in_DNS???}`
