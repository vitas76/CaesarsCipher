from CesarSifraModul2 import sifra, logocs

chod_prg = True
while chod_prg:
    print(logocs())
    volba = input("\nPro zakódování vyberte (E/e) pro dekódování vyberte (D/d) pro ukončení (Q/q).\n").lower()

    if volba == "q":
        print("Brzy na viděnou při kódování textu ;)")
        chod_prg = False
        break
    elif volba == "e":
        encode_decode = True
        enc_dec_str = "zakódování"
        enc_dec_str2 = "Zakódovaný"
    elif volba == "d":
        encode_decode = False
        enc_dec_str = "rozkódování"
        enc_dec_str2 = "Rozkódovaný"
    else:
        print("Pokud neumíte zvolit jedno ze tří písmen raději vypněte PC :(")
        chod_prg = False
        break

    slovo = input(f"Zadejte slovo/větu pro {enc_dec_str}:\n").lower()
    posun = int(input("Zadejte číslo pro posun:\n"))
    print(f"{enc_dec_str2} text:{sifra(slovo, posun, encode_decode)}")  # "vwxyz", 3 / "yzabc", 3

# TODO kodování dekodování do/ze souboru
