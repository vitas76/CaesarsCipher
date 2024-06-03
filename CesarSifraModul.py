# *** Cesarova šifra jako modul ***
alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# VZOR: slovo = "yzabc" / "vwxyz" ; kodovani = 3
# Pouziti encode("vwxyz", 3) / decode("yzabc", 3)


def encode(slovo, kodovani):
    zakodovano = ""
    for znak in slovo:
        index = alphabet.index(znak)
        newindex = (index + kodovani) % len(alphabet)
        zakodovano += alphabet[newindex]
        # print(f" {index} idex | newindex {newindex}")
    return zakodovano


def decode(slovo, kodovani):
    return encode(slovo, - kodovani)
