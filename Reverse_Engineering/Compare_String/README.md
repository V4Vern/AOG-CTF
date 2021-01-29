
# Compare_String

Difficulty Level: Easy

It looks like there's a flag somewhere inside this binary. I need help to recover the flag. 

### Hints

- No hints


## Deployment

Compile the c program: gcc -o tracer generate/generate.c  and upload tracer in distrib to static file server.

- tracer
    - SHA1: f8e7db7b22fabc7ea8767c2f569deeb5146b2cca
    - ELF 64-bit LSB executable


## Solution

When performing `objdump -d recall`, we can observe that the strcmp library is called from the Global Offset Table: 
```
Disassembly of section .plt:

// Output truncated

0000000000001070 <strcmp@plt>:
    1070:	ff 25 c2 2f 00 00    	jmpq   *0x2fc2(%rip)        # 4038 <strcmp@GLIBC_2.2.5>
    1076:	68 04 00 00 00       	pushq  $0x4
    107b:	e9 a0 ff ff ff       	jmpq   1020 <.plt>
```

We also observe that the `strcmp` library is used just before the success message is printed out in the disassembly of the main function:

```
0x00001290      call sym.imp.fgets ; char *fgets(char *s, int size, FILE *stream)
0x00001295      mov  rax, qword [s1]
0x00001299      lea  rdx, [s2]
0x0000129d      mov  rsi, rdx ; const char *s2
0x000012a0      mov  rdi, rax ; const char *s1
0x000012a3      call sym.imp.strcmp ; int strcmp(const char *s1, const char *s2)
0x000012a8      test eax, eax
0x000012aa      jne  0x12ba
0x000012ac      lea  rdi, str.Splendid__You_got_the_flag ; 0x2039 ; "Splendid! You got the flag!" ; const char *s
0x000012b3      call sym.imp.puts ; int puts(const char *s)
0x000012b8      jmp  0x12c6
0x000012ba      lea  rdi, str.Sorry__but_that_wasn_t_the_flag._Ever_get_that_feeling_of_d__j___vu ; 0x2058 ; "Sorry, but that wasn't the flag. Ever get that feeling of d\u00e9j\u00e0 vu?" ; const char *s
0x000012c1      call sym.imp.puts ; int puts(const char *s)
0x000012c6      mov  eax, 0
```

Hence, we can use the `ltrace` function to intercept and print the library calls of the program by running `ltrace ./recall`. By doing so, we can find out what strings are being compared in the `strcmp` function.

```
printf("Hey there! Help me recover the f"...Hey there! Help me recover the flag! - Tracer
)                                                                        = 48
fgets(> 
"\n", 29, 0x7ff3bc9e4860)                                                                                      = 0x7fff3ed3c7b0
strcmp("\n", "	19C4{r3v3r51n6_7hr0u6h_71m3}\n")                                                                        = -89
puts("Sorry, but that wasn't the flag."...Sorry, but that wasn't the flag. Ever get that feeling of déjà vu?
)                                                                          = 69
+++ exited (status 0) +++
```

ltrace is a library call tracer and it is primarily used to trace calls made by programs to library functions. Thus, it was able to trace to library functions such as fgets and strcmp. From here, we can see that I typed a string “test” in the fgets section and it immediately compared the string “test” with the variable “19C4….”



### Flag
`19C4{r3v3r51n6_7hr0u6h_71m3}`
