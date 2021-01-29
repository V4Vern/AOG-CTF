
# Redacted

Difficulty Level: Warmup
John has recently purchased a CCTV and he needs to find the password and the username to log in to the web interface. However, a hacker appears to have intercepted his email and did something to the document. Find the password and the username :)

### Hints

No hints are provided

## Deployment

Run Upload CCTV_Credentials.pdf in distrib to static file server.

- box.pdf
    - SHA1: 0d5fd7d16321e00f4d4aee9012fcd621d7086bf8
    - PDF file containing redacted username and password fields.


## Solution

PDF files can be viewed as many layers, the most bottom layer being the text in the PDF document. Hence, even if the text is redacted by Microsoft Word for example, the text itself will remain unchanged in the PDF. Therefore, we can select the text in the password field and copy-paste it to a text editor to reveal the flag.

### Flag
`19C4{Y0u_F0und_ReAdacted}`
