# *** Cesarova šifra jako modul ***
# Source of graphic logo: http://www.patorjk.com/software/taag/#p=testall&f=Graffiti&t=CaesarsCipher
# Source of code inspiration : https://youtu.be/BWtRPpGj-vw?list=PLQ8x_VWW6AktSriRsoH7LH_-t0LqS6aa_
# And thanks for the support Martin T.

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
