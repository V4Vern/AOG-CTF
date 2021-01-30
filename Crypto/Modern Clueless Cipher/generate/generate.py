def repeated_key_xor(plain_text, key):
    # returns plain text by repeatedly xoring it with key
    plain_text = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(plain_text)):
        encoded.append(plain_text[i] ^ key[i % len_key])
    return bytes(encoded)


def main():
    plain_text = b'19C4{repeated_key_xor}'
    key = b'ICE'

    ciphertext = repeated_key_xor(plain_text, key).hex()
    result = ""
    for i in range(0, len(ciphertext), 2):
        result += ciphertext[i:i + 2] + 'f'

    print("Plain text: ", plain_text)
    print("Key: ", key.hex())
    print("Encrypted as: ", result)


if __name__ == '__main__':
    main()
