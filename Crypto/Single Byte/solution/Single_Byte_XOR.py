#!/usr/bin/env python3

import sys
import binascii


if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

encoded = "212953246b206821204f21254f7d694f7624662065622127234f726927756d"
encoded = binascii.unhexlify(encoded)
for xor_key in range(256):
    decoded = ''.join(chr(b ^ xor_key) for b in encoded)
    if decoded.isprintable():
        print(xor_key, decoded)