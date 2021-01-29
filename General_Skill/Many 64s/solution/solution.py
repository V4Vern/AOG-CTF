import base64

with open("Crypto_5.txt",encoding = 'utf-8') as file:
    cipher_text= file.read()
    while True:
        try:
            cipher_text = base64.b64decode(cipher_text)
        except Exception as e:
            print(cipher_text)
            break
