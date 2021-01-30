
# TimeTravel 

Difficulty Level: Medium

You've heard that the Silicon Valley giant Business Factory Inc is about to make an announcement that could shake up the stock market and decide that you want in on some insider trading action. Business Factory has a website where they post their press releases, and they have the habit of putting announcements up in advance and merely toggling the visibility to the public when the release is scheduled to go out. Can you get access to their latest press release before everyone else does and make some $$$?

Connect at http://web.ctf-fun.xyz:15012



### Hints

- There's no admin panel to attack here; the attack is on view.php itself.
- No specialised trickery needed here; some quick maths is all you need.
- Do you see a pattern in the URLs for press releases?


## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

The attack here is a classic [Insecure Direct Object Reference]. In this case, view.php does not check to verify whether the public is allowed to access a specified press release, so even if a "hidden" press release isn't linked to from index.php, it can be accessed by guessing the "id" parameter. To solve the challenge, go to http://host/view.php?id=100 and retrieve the flag `19C4{i+s_Just_arithmetic}`


### Flag
`19C4{i+s_Just_arithmetic}`
