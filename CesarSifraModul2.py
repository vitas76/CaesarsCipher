# *** Cesarova šifra jako modul ***
alphabet = [' ', '.', ',', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# VZOR: slovo = "yzabc" / "vwxyz" ; kodovani = 3; enc_dec = True/False (Encoding/Decoding)
# Pouziti encode("vwxyz", 3) / decode("yzabc", 3)


def sifra(slovo, kodovani, enc_dec):
    zakodovano = ""
    for znak in slovo:
        index = alphabet.index(znak)
        if enc_dec:
            newindex = (index + kodovani) % len(alphabet)
            zakodovano += alphabet[newindex]
        elif not enc_dec:
            newindex = (index - kodovani) % len(alphabet)
            zakodovano += alphabet[newindex]
        # print(f" {index} idex | newindex {newindex}")
    return zakodovano


def logocs():
    logo = '''
    ┏┓          ┏┓   ┓     
    ┃ ┏┓┏┓┏┏┓┏┓┏┃ ┓┏┓┣┓┏┓┏┓
    ┗┛┗┻┗ ┛┗┻┛ ┛┗┛┗┣┛┛┗┗ ┛ 
                   ┛       
    '''
    return print(logo)
