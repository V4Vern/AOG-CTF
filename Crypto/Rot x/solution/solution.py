from string import ascii_lowercase, ascii_uppercase

c = "Ypw'zj zwufpp hwyj vltlqm cicopjtnm! Etr ubry cn 19B4{eucuzv_rc_rhb_aaiejovv}. Oqz lka xee fcbu hxh wkb pbrhv lvz dsq ftik hz pecl, vkid dww'e nza sw ncep data :)."

def decrypt(ct):
    out = ''
    for i,c in enumerate(ct):
        if c in ascii_lowercase:
            alph = ascii_lowercase
        elif c in ascii_uppercase:
            alph = ascii_uppercase
        else:
            out += c
            continue
        out += alph[(alph.index(c) - i) % len(alph)]
    return out

print(decrypt(c))
