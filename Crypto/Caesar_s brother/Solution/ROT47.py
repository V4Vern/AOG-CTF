data = "pAA=J:?8 #~%`b E@ 2 A:646 @7 E6IE >6C6=J C6BF:C6D 6I2>:?:?8 :ED 2=A9236E:4 492C24E6CD 2?5 C6A=24:?8 6249 @?6 " \
       "3J E96 =6EE6C `b A=246D 7FCE96C 2=@?8 :? E96 2=A9236E[ HC2AA:?8 324< E@ E96 368:??:?8 :7 ?646DD2CJ]%96 7=28 :D " \
       "Q(62<0r:A96C] p 364@>6D }[ q 364@>6D ~[ 2?5 D@ @? FA E@ |[ H9:49 364@>6D +[ E96? E96 D6BF6?46 4@?E:?F6D 2E E96 " \
       "368:??:?8 @7 E96 2=A9236Ei } 364@>6D p[ ~ 364@>6D q[ 2?5 D@ @? E@ +[ H9:49 364@>6D |] ~?=J E9@D6 =6EE6CD H9:49 " \
       "@44FC :? E96 t?8=:D9 2=A9236E 2C6 27764E65j ?F>36CD[ DJ>3@=D[ H9:E6DA246[ 2?5 2== @E96C 492C24E6CD 2C6 =67E " \
       "F?492?865] q642FD6 E96C6 2C6 ae =6EE6CD :? E96 t?8=:D9 2=A9236E 2?5 ae l a × `b[ E96 #~%`b 7F?4E:@? :D :ED @H? " \
       ":?G6CD6] Q "


def rot47(cipher):
    x = []
    for i in range(len(data)):
        j = ord(data[i])  # The number of the character in ASCII
        if 33 <= j <= 126:  # Characters used for ROT47 encoding have an ASCII value range of 33-126
            x.append(chr(33 + ((j + 14) % 94)))
    else:
        x.append(data[i])

    a = "".join(x)
    print(a)


rot47(data)
