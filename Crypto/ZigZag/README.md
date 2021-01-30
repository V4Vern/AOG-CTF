
# ZigZag

Difficulty Level: Warmup

Pete zigzagged several times , and fell off at the 7 rails. Peter then uses scytale to craft this ciphertext. Decode the following: ecc__rncsareiicafp_kei_hralleb to get the secret text. 

The flag format is in the form of 19C4{secret text}


### Hints

- No hints are given


## Deployment

- No deployment needed


## Solution

With Rail Fence Cipher solver at https://www.boxentriq.com/code-breaking/rail-fence-cipher, paste the ciphertext and attempt to break the cipher with the following configurations:
 - Rails: 7
 - Offset: 3


### Flag
`19C4{rail_fence_cipher_is_crackable}`
