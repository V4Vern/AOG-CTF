#!/usr/bin/env python3
import random
from string import ascii_lowercase

non_hex = "".join(list(ascii_lowercase)[6:])
flag = "5313943347b72333633785f31355f6d795f623335375f667231336e647d"
final_str = ""

for hexadecimal in flag:
    final_str += "".join(random.choices(non_hex, k=random.randint(1, 10))) + hexadecimal

with open("flag.txt", "w") as fp:
    fp.write(final_str)
