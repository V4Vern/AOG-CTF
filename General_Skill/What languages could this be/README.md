
# What languages could this be

Difficulty Level: Medium

My Brain hurts after looking at this programming language…..

### Hints

- Upload Language1.png and Language2.png to the hint section. 
- There could be more than one similar programming languages 


## Deployment

Upload language.txt in distrib to static file server. 

- language.txt
    - SHA1: 1709a4085d1ee6def3776757b5c3e8d31cfd9104
    - Text file containing encrypted strings


## Solution

"An esoteric programming language, or esolang, is a computer programming language designed to experiment with weird ideas, to be hard to program in, or as a joke, rather than for practical use.”

We are given a brainfk to decode where we can decode it using https://www.dcode.fr/brainfuck-language. After decoding the brainfuck, we will need to further decode it using reversefuck at https://www.dcode.fr/reversefuck-language to get the flag


### Flag
`19C4{Reverse_F}`
