import random
from string import ascii_letters, digits

character_list = ascii_letters + digits
flag = "19C4{Look_Carefully}"


with open("Hunt the Mouse.txt", "w") as file:
    for line in range(10000):
        if line == 7562:
            file.write(flag+"\n")
        ran_str = ""
        for char in range(20):
            ran_str += random.choice(character_list)
        ran_str += "\n"
        file.write(ran_str)


