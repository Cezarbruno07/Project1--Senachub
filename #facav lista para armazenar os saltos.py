#facav lista para armazenar os saltos 
""" Primeiro salto 6.5 m
sergundo salto :6.1 m
Terceiro salto 
Quarto Salto : 5.4m
Quinto Salto :5.3

Melhor Salto : 6.5 m
Pior Salto: 5.9 m
"""

atletas +[]
while True :
    nome = input("Digite onome do atleta (ou enter para encerrar o programa ):")
    if nome == "":
        break
    atleta ={"nome": nome,
             "Saltos":[],
             "media": 0,
             "pior_salto": 0,}
    for i in range(5):
        atleta.get("saltos").append(float(input(f"Distancia do {i+1}º salto:")))
        atleta.get("saltos").sort() # ? ordena a lista 
        atleta["pior_salto"] = atleta.get("saltos").pop(0)
        atleta["melhor_salto"] = atleta.get("saltos").pop()
        atleta["media"]= sum(atleta.get("saltos)"))/3

    print(f"\nMelhor salto: {atleta.get('Melhor salto')}")

    