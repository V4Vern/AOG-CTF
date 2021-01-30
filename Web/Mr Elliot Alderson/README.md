
# Mr Elliot Alderson

Difficulty Level: Easy

Mr Robot, one of the most realistic hacking American drama thriller television series. It stars Rami Malek as Elliot Alderson, a cybersecurity engineer and hacker with social anxiety disorder and clinical depression. Elliot is recruited by an insurrectionary anarchist known as "Mr. Robot", played by Christian Slater, to join a group of hacktivists called "fsociety". The group aims to destroy all debt records by encrypting the financial data of E Corp, the largest conglomerate in the world.

Connect at http://web.ctf-fun.xyz:15011


### Hints

- -	No hints are given.

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

When you google the challenge title or even the challenge text will tell that this is about Mr. Robot. This indicates that the user might want to check out the robots.txt for the website. 
When you open the website, it serves the index.html file, which has content written about Mr Robot, again trying to put across robots.txt. When you visit robots.txt, you see:

Hey there, you're not a robot, yet I see you sniffing through this file.
SEO you later!
Now get off my lawn.
User-Agent: *
Disallow: /Do_Not_Access.html

When you visit the disallowed route, you get the flag!

### Flag
`19C4{e1i$ot_@lDerson}`
