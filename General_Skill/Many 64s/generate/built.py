import base64

num_of_encoding = []
flag = "19C4{L00p-Base64}"
encoded = base64.b64encode(flag.encode("utf-8"))
num_of_encoding.append(encoded)

for num_of_times in range(49):
    num_of_encoding.append(base64.b64encode(num_of_encoding[num_of_times]))

with open("Crypto_5.txt", "w") as file:
    file.write(num_of_encoding[-1].decode("utf-8"))
