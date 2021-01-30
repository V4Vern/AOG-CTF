def repeated_key_xor(plain_text, key):
    # returns plain text by repeatedly xoring it with key
    plain_text = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(plain_text)):
        encoded.append(plain_text[i] ^ key[i % len_key])
    return bytes(encoded)


def main():
    cipher = bytes.fromhex("787a067d38372c33202837202d1c2e2c3a1a312c3734")
    plain_text = cipher
    key = bytes.fromhex("494345")

    print("Plain text: ", repeated_key_xor(plain_text, key))


if __name__ == '__main__':
    main()
