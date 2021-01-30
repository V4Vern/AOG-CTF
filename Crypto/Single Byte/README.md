
# Single Byte 

Difficulty Level: Medium

I encrypted my data with a single byte using a bitwise operator which returns 0 if the bits are the same, and 1 otherwise which can also be represented using ^ in most programming languages.

Decode the following ciphertext to get the flag:

212953246b206821204f21254f7d694f7624662065622127234f726927756d


### Hints

- XOR Single Byte


## Deployment

No deployment needed

## Solution

The Single-byte XOR cipher algorithm works with an encryption key of size 1 byte - which means the encryption key could be one of the possible 256 values of a byte.

As part of the encryption process, the original message is iterated bytewise and every single byte b is XORed with the encryption key key and the resultant stream of bytes is again translated back as characters and sent to the other party. These encrypted bytes need not be among the usual printable characters and should ideally be interpreted as a stream of bytes.

As an example, we can try to encrypt the plain text - abcd - with encryption key 69 and as per the algorithm, we perform XOR bytewise on the given plain text. For character a, the byte i.e. ASCII value is 97 which when XORed with 69 results in 36 whose character equivalent is $, similarly for b the encrypted byte is ', for c it is & and for d it is !. Hence when abcd is encrypted using single-byte XOR cipher and encryption key 69, the resultant ciphertext i.e. the encrypted message is $'&!.

Decryption is the process of extracting the original message from the encrypted ciphertext given the encryption key. XOR has a property - if a = b ^ c then b = a ^ c, hence the decryption process is exactly the same as the encryption i.e. we iterate through the encrypted message bytewise and XOR each byte with the encryption key - the resultant will be the original message.

There are a very limited number of possible encryption keys - 256 to be exact - we can, very conveniently, go for the Bruteforce approach and try to decrypt the ciphered text with every single one of it. So we start iterating over all keys in the range [0, 256) and decrypt the ciphertext and see which one resembles the original message the most.

### Flag
`19C4{0x10_15_my_f4v0ur173_by7e}`
