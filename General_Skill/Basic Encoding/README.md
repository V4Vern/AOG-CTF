
# Basic Encoding

Difficulty Level: Easy

This encoding is a binary-to-text encoding schemes that represent binary data (more specifically a sequence of 8-bit bytes) in an ASCII string format by translating it into a radix-64 representation

Decode the following encoding:

d7d0b8fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f79e7bf

### Hints

- Take the below hex string, decode it into bytes and then encode it into Base64.
- After decoding to bytes, encode it to base64 to get the flag.

## Deployment

No deployment are needed 

## Solution

The challenge text is encoded in hex format which needs to be then decoded into bytes and then encoded into Base64.

### Flag
`19C4{Base+64+Encoding+is+Web+Safeee}`
