#!/usr/bin/env python3

import sys

# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

hex_string = "313943347b4865785f49535f4261736531367d"
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print("Here is your flag:")
print(ascii_string)