
# T-Rex

Difficulty Level: Easy

My friend complained to me that when he searches for the T-Rex game on Google, some weird spam shows up as the result text beside his page, but when I go to his site nothing seems amiss. Is Google seeing something different than I am?!

Connect at http://web.ctf-fun.xyz:15012


### Hints

- Maybe Google sends something when crawling the page that causes the website to behave differently... 

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

When Google crawls websites, it sets its [User Agent] to include the string ["Googlebot"] If a website has code to detect this user agent, it can make Google see the site differently from a regular user.

To solve this challenge, [change your user agent] to include the string "Googlebot". The resulting extra text that shows up should include the flag, `19C4{im_in_ur_php_poisoning_ur_seo}`

### Flag
`19C4{im_in_ur_php_poisoning_ur_seo}`
