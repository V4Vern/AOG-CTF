
# Redirect

Difficulty Level: Warmup

I want to access the secret site but it keeps redirecting me to another website

Connect at http://web.ctf-fun.xyz:15010


### Hints

- -	No hints are given.

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

This web challenge can be solved via using a web proxy “burpsuite” where you have control whether to forward the redirected request or not. By not forwarding the redirected request, you can then view the flag at the bottom of the site.

### Flag
`19C4{Keep-mov1ng-4!way}`
