
# Blog

Difficulty Level: Medium

Can you try to help me debug this blog?

Connect at http://web.ctf-fun.xyz:15014/


### Hints

- No hints are provided


## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

Simple blog consisted of a single webpage with no dynamic content.

The key to the challenge was to notice a X-Debug header in the server response :
< HTTP/1.1 200 OK
< Date: Thu, 09 Nov 2017 14:10:44 GMT
< Server: Apache/2.4.10 (Debian)
< X-Powered-By: PHP/7.0.23
< X-Debug: false
< Vary: Accept-Encoding
< Content-Length: 5232
< Content-Type: text/html; charset=UTF-8

In fact, all the headers here were common with the exception of X-Debug.
Since the header is set to false, our goal is to set it to true and see what happens.
We can do this by sending a request with a X-Debug: true header. If done properly, the webapp gives us the source code!
Here's the important part :
<?php
  if ($_GET['i_want_a'] == 'flag') {
    echo $flag;
    echo "<br><img src='img/cat.jpg'>";
  }
?>

So all we have to do is send a request to http://web.ctf-fun.xyz:15014/?i_want_a=flag in order to obtain our flag.

$ curl http://web.ctf-fun.xyz:15014/?i_want_a=flag | grep 19C4


### Flag
`19C4{XDEBUG_DEBUGGING}`
