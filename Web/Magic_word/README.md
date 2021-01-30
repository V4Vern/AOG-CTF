
# Magic_word

Difficulty Level: Medium

Can you try to find a way to submit the magic word?

Connect at http://web.ctf-fun.xyz:15009/


### Hints

- No hints are provided


## Deployment

Run  sudo ./build.sh in distrib to static file server.

## Solution

This challenge demonstrates a very common bypass that you can find in webapp security.

The gist of the challenge is the following :

The app takes a word from the user through the `?magic_word=` argument.

It then replaces all instances of `bumfuzzle` with an empty string. Finally, it checks if `bumfuzzle` is still there, even after the replacements.

This is the behavior described above :
```
preg_replace("/bumfuzzle/", "", "hello") // Returns "hello"
preg_replace("/bumfuzzle/", "", "hellobumfuzzle") // Returns "hello"
preg_replace("/bumfuzzle/", "", "bumfasdfuzzle") // Returns "bumfasdfuzzle"
```

Since `bumfuzzle` is removed, a simple trick we can use is to embed `bumfuzzle` inside `bumfuzzle`.

The solution is the following :

preg_replace("/bumfuzzle/", "", "bumfbumfuzzleuzzle") // Returns "bumfuzzle"

You can find the flag by visiting this URL : `http://web.ctf-fun.xyz:15009/?magic_word=bumfbumfuzzleuzzle`.



### Flag
`19C4{bumfuzzle_fuzzlebum}`
