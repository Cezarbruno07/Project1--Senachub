

import math

#Funções
def func(situacoes):
    situacoes = eval(input("""Para comprar apenas latas de 18 litros digite 1
Para comprar apenas galões de 3,6 litros digite 2
Para misturar latas e galões, de forma que o preço seja o menor digite 3
Digite o a opção desejada: """))
    while not 1 <= situacoes <= 3:    
        situacoes = eval(input("Digite um opção de 1 à 3: "))
    if situacoes == 1:
        print()
        print("Você precisará de %d litros de tinta, %d latas e pagará R$ %d" % (litrosf,latas,preco_latas))
        print()
    elif situacoes == 2:
        print()
        print("Você precisará de %d litros de tinta, %d galoes e pagará R$ %d" % (litrosf,galoes,preco_galoes))
        print()
    elif situacoes == 3:
        a1 = int(litrosf/18)
        a2 = litrosf%18
        a3 = math.ceil(a2/3.6)
        a4 = ((a1*80)+(a3*25))
        print("Você de %d litros de tinta, %d latas, %d galões e pagará R$ %d" % (litrosf,a1,a3,a4))      
    else:
         return situacoes
    print()

def menu(a):
    print("Suas opções são:")
    print("")
    print("1) Calcular a área a ser pintada")
    print("2) Preços dos produtos")
    print("3) Calcular os preços por área a ser pintada")
    print("4) Sair do programa")
    print()
    opcao = eval(input("Escolha sua opção: "))
    while not 1 <= opcao <= 4:
        print()
        opcao = eval(input("Escolha uma opção de 1 a 4: "))
    else:
        return opcao
            

def precos(a):
    print()
    print("Temos latas de 18 litros e galões ")
    print("Cada lata custa R$80 e cada galão R$25")
    print()

    

print("Seja bem vindo a Sertão")
loop = 1
choice = 0
area = 0
while loop:
    choice = menu(1)
    if choice == 1:
        area = eval(input("Tamanho em metros quadrados (m²) da área a ser pintada: "))
        litros = float(area/6)
        litrosf = math.ceil(float(litros*1.1))
        latas = math.ceil(float(litrosf) / 18)
        galoes = math.ceil(float(litrosf) / float(3.6))
        preco_latas = latas*80.0
        preco_galoes = galoes*25.0
        tinta_necessaria = float(area)/6
        lata = 18.0
        galao = 3.6
        limit = 108
        x = area - limit
        y = x/6
        y1 = math.ceil(float(y*1.1))
        
    elif choice == 2:
        precos(1)
    elif choice == 3:
        if area == 0:
            print()    
            print("Execulte primeiro a opção 1 [Calcular a área]!")
            print()
        else:
            func(1)
    elif choice == 4:
        loop = 0

print()        
print("Volte sempre!")
        

                 
                                            

