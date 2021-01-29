
# Messy	

Difficulty Level: Medium

I was playing with some hexadecimals when someone accidentally mixed junk data in my text file. Help me retrieve the flag! This is not a regular thing

### Hints

- Some people tell me that my expressions aren't really regular
- Regular Expression helps



## Deployment

Run ./generate/build.py to generate flag.txt

- ●	flag.txt
    - SHA1: 5457b34323ed9012c6eb1b4eb1b9465f42c836b5
    - ASCII Text



## Solution

Use a regex to find the characters in the file that belong to base-16, afterwards decode it to get the flag. 
Cyberchef recipes can be found "https://gchq.github.io/CyberChef/#recipe=Regular_expression('User%20defined','%5B0-9a-f%5D',true,true,false,false,false,false,'List%20matches')From_Hex('Auto')"

### Flag
`19C4{r363x_15_my_b357_fr13nd}`
