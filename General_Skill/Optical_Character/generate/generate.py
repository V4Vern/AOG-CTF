import random
import string
import codecs

flag = "Test_CTF{Opt1ca!_ch@r@cter_recognition}"

with open("flag.txt", "w") as file:
    for line in range(300):
        if line == 222:
            encoded_flag = codecs.encode(flag, 'rot_13').encode()
            file.write(codecs.encode(encoded_flag, "hex").decode() + "\n")
            continue
        ran_list = "".join(random.choices(string.ascii_letters + string.digits, k=38))
        ran_str = ran_list[:8] + "{" + ran_list[8:14] + "_" + ran_list[14:22] + "_" + ran_list[22:35] + "}"
        file.write(codecs.encode(ran_str.encode(), "hex").decode() + "\n")
