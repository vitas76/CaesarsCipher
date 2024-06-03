
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

slovo = "vwxyz"
kodovani = 23
zakodovano = ""
for znak in slovo:
    index = alphabet.index(znak) + 1
    if (index + kodovani) > (len(alphabet)):
        real_code = (index + kodovani - 1) - (len(alphabet))
    else:
        real_code = index + kodovani - 1
    print(real_code)
    zakodovano += alphabet[real_code]
    print(f" {index} idex | realyc {real_code}")
print(zakodovano)

print(len(alphabet))
# for znak in range(len(alphabet)):
#     print(znak + 1)
#     # index = alphabet.index(znak)
