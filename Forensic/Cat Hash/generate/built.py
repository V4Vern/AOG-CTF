import random
from string import ascii_letters, digits

# This generates a character list with all the possible alphanumeric characters
character_list = ascii_letters + digits
flag = "19C4{4ccur4cy!sb5d}"

with open("lookup.list", "a") as file:
    for line in range(100000):
        if line == 85232:
            file.write(flag + "\n")
        rand_str = ""
        for char in range(17):
            rand_str += random.choice(character_list)
        rand_str = "19C4{" + rand_str + "}\n"
        file.write(rand_str)

