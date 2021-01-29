
# Protection

Difficulty Level: Hard

This binary has some protection on the advanced 64 bit shellcode. Help me find it.

### Hints

- No hints


## Deployment

Execute the program to compile the file via: ./make  and upload Protection in distrib to static file server.

- Protection
    - SHA1: f8e7db7b22fabc7ea8767c2f569deeb5146b2cca
    - ELF 64-bit LSB executable


## Solution

This challenge is about reverse engineering encrypted shellcode. It includes a snippet of hand written shellcode, encrypted with a very typical xor + add encoding algorithm, and finally injected into memory via `mmap` and `memcpy` to execute. Firstly, we can decompile the program via gihdra:
So you can see by the labeled sections above that memcpy was called on the code to the `__dest` location before it was executed. This is because anything encrypted has to be decrypted before it executes, which is the nature of all malware.

Now we run it in gdb: “gdb -q ./protection”. Starting off with disassembling the main function, to identify where to set our breakpoints via “disass main”

So at main+299, the shellcode would've been fully decrypted and copied into memory. We set the breakpoint there.

now we have hit our breakpoint, we can step through one by one via “ni”.

And at this point, "Can u find the flag?" is printed and gdb exits. Interesting. Doing that again, but this time without `ni`, and just looking at what gets executed. We inspect 20 instructions (`x/20i` at the register `rdx`, because that's where the call goes in main (`callq  *%rdx`)

Here we see a bunch of stuff being pushed into memory. Cool.
Extracting the data out of it:
7664617b34433931
6e455f6465636e34
7364337470797263
33646f436c6c6568
662075206e61437d
2065687420646e69
2020203f67616c66

We can decode the following hex into ascii characters via cyberchef: 
“vda{4C91nE_decn4sd3tpyrc3doCllehf u naC} eht dni   ?galf”
Upon reversing the text, we can see some of the fragments of the flag :
flag?   ind the }Can u fhellCod3crypt3ds4nced_En19C4{adv
Now it's still little endian because it was pushed onto the stack "upside down". We can manually reverse this, 8 chars at a time:
19C4{adv4nced_Encrypt3dshellCod3}Can u find the flag?


### Flag
`19C4{adv4nced_Encrypt3dshellCod3}`
