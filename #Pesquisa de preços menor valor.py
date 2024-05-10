#Pesquisa de preços menor valor 
preco1 = float(input("Digite no preço arroz no Comper : "))
preco2 = float(input("Digite o preço do Arroz no Atacadão: "))
preco3 = float(input("Digite o preço do Arroz no Fort : "))
if preco1 < preco2 and preco1 < preco3:
    print(f"O Arroz mais Barato é do Comper , custando R${preco1:.2f}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"O Arroz mais barato é do Atacadão , custando R${preco2:.2f}")
else:
    print(f"o Arroz mais barato é do Fort , custando R${preco3:.2f}")