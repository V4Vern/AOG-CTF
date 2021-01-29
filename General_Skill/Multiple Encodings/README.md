
# Mutliple Encodings

Difficulty Level: Easy

My friend said that multiple bases of encodings make it more secure. 

### Hints

- The first encoding is similar to the previous encoding challenges.
- You might need to guess the second encoding to see decimal numbers
- Decimal numbers is also a type of encoding 


## Deployment

Upload Multiple Encodings.txt in distrib to static file server.

- Multiple Encodings.docx
    - SHA1: 9140d251ca8cb68b9ae7640bd96e471519849db8
    - Text file containing encoded strings


## Solution

The flag is encoded Base10 > Base32 > Base64, to get the flag just inverse the operations.

https://gchq.github.io/CyberChef/

Recipe: From_Base64('A-Za-z0-9+/=',true)
		From_Base32('A-Z2-7=',true)
		From_Decimal('Space',false)

### Flag
`19C4{Multiple_Encoding}`
