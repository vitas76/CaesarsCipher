from CesarSifraModul import encode, decode

chod_prg = True
while chod_prg:
    volba = input("\nPro zakódování vyberte (E/e) pro dekódování vyberte (D/d) pro ukončení (Q/q).\n").lower()
    if volba == "q":
        print("Brzy na viděnou při kódování textu ;)")
        chod_prg = False
        break
    elif volba == "e":
        slovo_en = input("Zadejte slovo/větu pro zakódování:\n").lower()
        posun_en = int(input("Zadejte číslo pro posun:\n"))
        print(f"Zakódovaný text: {encode(slovo_en, posun_en)}")  # "vwxyz", 3
    elif volba == "d":
        slovo_de = input("Zadejte slovo/větu pro rozkódování:\n").lower()
        posun_de = int(input("Zadejte číslo pro posun:\n"))
        print(f"Rozkódovaný text: {decode(slovo_de, posun_de)}")  # "yzabc", 3
    else:
        print("Pokud neumíte zvolit jedno ze tří písmen raději vypněte PC :(")
        chod_prg = False
        break
