import emoji

resposta =input("Teste ?(f/T):")

if resposta.upper() == 'F':
    print(emoji.emojize("fico Feliz"))
elif resposta.upper() == 'T':
    print(emoji.emojize("Fico Triste"))
else:
   print("Resposta")