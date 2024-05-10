letra = input("Digite uma letra: ").upper()
loop=letra
if (
    letra == "A"
    or letra == "E"
    or letra == "I"
    or letra == "O"
    or letra == "U"
):
    print("Vogal")
else:
    print("Consoante")