#!/usr/bin/env python3

import sys

# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [49,57,67,52,123,65,83,83,45,75,69,89,95,73,83,95,65,83,67,73,73,125]

print("Here is your flag:")
print("".join(chr(o) for o in ords))
