#!/usr/bin/env python3
import base64
import sys

# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

hex_string = "d7d0b8fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f79e7bf"
bytes_object = bytes.fromhex(hex_string)
b64 = base64.b64encode(bytes_object)
print(b64)
