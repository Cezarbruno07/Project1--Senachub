# def hello():
#     print("Ola!!!")
    
# hello()


# def hello (nome):
#     print("Ola", nome)
# hello ("Ederson")


# def hello(nome):
#     print("Seja Bem - Vindo",nome)

# a=input("Digite seu nome = ")

# hello(a)


# def hello (nome):
#     print("Ola",nome)

# hello ('Ederson')
# hello ('Bruno')
# hello ('Cezar')

# def fareheit(temp):
#     return ((temp-32) *(5/9))    

                    
# def hello (nome , idade ):
#     print("ola" ,nome ,'\n Sua idade é :', idade)


# hello ("Ederson", 25)

def calcular_pagamento(qtd_horas,valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas<=40:
        salario=horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    print(salario)


hora = input("Digite horas ")
valor= int(input("Digite o Valor da hora"))
calcular_pagamento(hora,valor)
