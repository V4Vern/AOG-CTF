
# MiniComputer
Difficulty Level: Hard

This time, I generated a larger prime to prevent anyone from decrypting

### Hints

- Small exponent is vulnerable to an attack


## Deployment

Run ./generate/generate.py to generate flag.txt

- flag.txt
    - SHA1:  
    - Text file containing e, n and c 


## Solution

The idea here is that e=3 is pretty small whereas n is big, so it is possible that pow(m,e) is inferior to n. 

so c, which is pow(m,e,n) would probably simply be pow(m,e)=pow(m,3)  and so m = pow(c,1/3) ie cube root of c

The solution can be found in solution/solution.py.

### Flag
`19C4{N33d_m04R_p4dd1ng}`
