
# C2_Server

Difficulty Level: Hard

It's now midnight. We have found the HTTP server that the botnet is using. Find the secret that they are hiding. Decrypt and decode the secret and we can begin to bring down their whole operation.  

### Hints

- Check out this cool text for robots

## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

Nginx reveals its own configuration under `/config/` (Done intentionally). This is known by viewing the robots.txt file.  Nginx.conf shows a second virtual host / server. This is the one we will be interested in.    Use `curl` or other methods like `Postman` or `Insomnia` to specifially modify the host header in the HTTP requests. This will cause it to go to the virtual host. `eW91IGhhdmUgbGl0ZXJhbGx5IGJlZW4gYmFpdGVk.malwa.re.local`    
If you examine the conf, you realise only '`/`' is black holed.  View `/index.html` directly and you see that it links to `/bots.yaml`, which contains more links.  Additionally, `/robots.txt` plays a part as well.  `/bots.yaml` contains the decryption key used in the XOR later.  `/api/v1/secret` reveals the encrypted and encoded secret.  `/scripts/flag.py` is the Python3 script that can retrieve the secret from the server and decode it with a key specified in bots.yaml  


### Flag
`19C4{M2lwyre_1$_Interesting}`
