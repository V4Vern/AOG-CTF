
# Emordnilap

Difficulty Level: Easy

“Things aren't always what they seem.Our fears can play tricks on us, making us afraid to change course, afraid to move on, but usually, hidden behind our fears are second chances waiting to be seized, second chances at life, at glory, at family, at love. And these opportunities don't come around every day, so when they do, we have to be brave, take a chance, and grab them while we can.” ― Barry Allen "The Flash"

### Hints

- The title of the challenge itself is a hint
- The encoding is similar to the previous challenge


## Deployment

Upload Flash.gif in distrib to static file server.

-Flash.gif
    - SHA1: 86a980233df0b39ba7128071b52883fed4ef296c
    - GIF file containing reverse encoded string


## Solution

Base64 is a way to encode binary data into an ASCII character set known to pretty much every computer system, in order to transmit the data without loss or modification of the contents itself. For example, mail systems cannot deal with binary data because they expect ASCII (textual) data. So if you want to transfer an image or another file, it will get corrupted because of the way it deals with the data.

Extract the base64 encoded data in the gif and noticed that the data is spelled backwards according to the hint in the title. Reverse the data using http://spellbackwards.com/ and decode it using base64 to get the flag.

### Flag
`19C4{Base_64}`
