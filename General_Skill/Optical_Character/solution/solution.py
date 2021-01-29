from PIL import Image
import pytesseract
import codecs

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image = Image.open('flag-4.jpg')
text = pytesseract.image_to_string(image)
hex_list = text.split("\n")
for hexa in hex_list:
    try:
        decoded   = codecs.decode(hexa,'hex')
        plaintext = codecs.decode(decoded.decode(),'rot_13')
        if "Test_CTF" in plaintext:
            print("The flag is {0}".format(plaintext))
            break
    except ValueError:
        print("Skipped: {0}".format(hexa))
        continue