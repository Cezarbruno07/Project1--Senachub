""" num1= int(input("Digite um numero: "))
num2=int(input("Digite outro Numero: "))
soma= num1 + num2
print(f"a soma entre {num1}e{num2} e {soma} ") """

#CAlculo de notas informar a maior 
""" nota1=float(input("Digite a nota da unidade 1: "))
nota2=float(input("Digite a nota da Unidade 2: "))
nota3=float(input("Digite a nota da Unidade 3: "))
nota4=float(input("Digite a nota da Unidade 4: "))
media=(nota1+nota2+nota3+nota4)/4
print(f"A media de notas {nota1:.2f}, {nota2:.2f}," f"{nota3:.2f} e {nota4:.2f} é {media:.2f}") """

# Converter metros em centimetros
""" metros =float(input("Digite o Valor em Metros "))
centimetros=metros*100
print(f"{metros: .2f} Metros equivalem a {centimetros:.2f} Centimetros") """

#raio de circulo 
""" pi=3.1415926
raio=float(input("digite o raio do circulo "))
area=pi *(raio**2)
print(f" a Area de circulo de raio {raio} é {area:.2f}") """

""" num1 = float(input("Digite um numero : "))
num2= float (input("Digite outro numero : "))
if num1 >num2 :
    print(num1)
else:
    print(num2) """

#loja de tintas 

""" import math
metros_quadrados=float(input("digite os Metros m²"))
metros_quadrados_mais_dez = metros_quadrados *1.0
litros_lata=18
rendimento_litro = 6
preco_lata = 80
rendimento_lata = rendimento_litro * litros_lata
litros_galao=3.6
preco_galao=25
rendimento_galao = rendimento_litro * litros_galao

somete_latas = math.ceil(metros_quadrados /rendimento_galao)
somente_galoes = math.ceil(metros_quadrados /rendimento_galao)
latas= math.floor(metros_quadrados_mais_dez / rendimento_lata)
galoes =math.ceil(metros_quadrados_mais_dez % rendimento_lata)/rendimento_galao  

print(f"Somente Lats : {somete_latas},"
      f"custando R${somete_latas *preco_lata}\n"
      f"Somente Galoes :{somente_galoes},"
      f"Custando R${somente_galoes * preco_galao}\n"
      f"Latas: {latas} , Galoes:{galoes},"
      f"custando R${((latas * preco_lata)+(galoes*preco_galao)):.2f}") """

""" turno = input("Digite seu turno, M -matutino, V - Vespertino, N-noturno:").upper()
if turno == "M":
    print("Bom dia ")
elif turno=="V":
    print("Boa tarde ")
elif turno=="N":
    print("Boa noite ")

else:
    print("Valor invalido") """

#Salario exemplo 21

""" valor_da_hora=float(input("Digite o quanto voçe recebe por hora "))
horas_trabalhadas=float(input("Digite quantas horas voçe trabalhou esse mes :"))
salario_bruto =valor_da_hora *horas_trabalhadas
if salario_bruto <=900:
    desconto_ir=0.0
elif salario_bruto <=1500:
    desconto_ir=5
elif salario_bruto <= 2500:
    desconto_ir=10
else:
    desconto_ir=20
IR=salario_bruto*(desconto_ir/100)
INSS= salario_bruto*(10/100)
FGTS= salario_bruto*(11/100)
total_de_descontos=IR+INSS
salario_liquido=salario_bruto- total_de_descontos

print(f"\nSalario Bruto : R${salario_bruto:.2f}",
      f"\n(-) IR (5%) :R${IR:.2f}",
f"\n(-) INSS(10%) :R${INSS:.2f}",
f"\nFGTS(11%) :R${FGTS:.2f}",
f"\nTotal de descontos : R${total_de_descontos:.2}",
f"\nSalario Liquido : R${salario_liquido:.2f}",)
 """

#Numero inteiro ou decimal
""" num=float(input("Digite um numero " ))
if num %1==0:
    print("Inteiro")
else:
    print("Decimal") """

#Acougue 
""" carne=input("Digite F para File duplo , A Para Alcatra e P para Picanha : ")
peso=float(input("Quanto kilos vai comprar: "))
pagamento=(input("Dinheiro cartão vuon card (5% de Desconto)"))
preco_total=0

print("\nHiper Comper \nCupom fiscal\n")
if carne=="F" or carne=="f":
    print("Item: File Duplo")
    if peso >5:
        preco_total+peso*5.8
    else:
        preco_total=peso*4.9
elif carne=="A" or carne=="a":
    print("item: Alcatra")
    if peso >5:
        preco_total = peso *6.8
    else:
        preco_total=peso*5.9
elif carne =="P" or carne=="p":
    print("Item : Picanha")
    if peso >5:
        preco_total=peso*7.8
    else:
        preco_total=peso*6.9
print(f"quantidade :{peso:.2f}KG")
print(f"Preco total:R${preco_total:.2f}")
if pagamento == "D" or pagamento=="d":
    print("Tipo de Pagamento: dinheiro")
    desconto=0
    print(f"Desconto:R${desconto:.2f}")
    print(f"valor a pagar : R${(preco_total-desconto):.2f}")
elif pagamento == "C" or pagamento =="c":
    print("Tipo de Pagamento: Vuon Card")
    desconto=preco_total*5/100
    print(f"Desconto: R${desconto:.2f}")
 """
carne = input("Digite F para Filé duplo, A para Alcatra e P para Picanha: ").strip().upper()
peso = float(input("Quantos quilos vai comprar: "))
pagamento = input("Tipo de pagamento (D para Dinheiro, C para Vuon Card - 5% de Desconto): ").strip().upper()
preco_total = 0

print("\nHiper Comper\nCupom Fiscal\n")

if carne == "F":
    print("Item: Filé Duplo")
    if peso > 5:
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9
elif carne == "A":
    print("Item: Alcatra")
    if peso > 5:
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9
elif carne == "P":
    print("Item: Picanha")
    if peso > 5:
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9

print(f"Quantidade: {peso:.2f} KG")
print(f"Preço Total: R${preco_total:.2f}")

desconto = 0
if pagamento == "D":
    print("Tipo de Pagamento: Dinheiro")
elif pagamento == "C":
    print("Tipo de Pagamento: Vuon Card")
    desconto = preco_total * 0.05
    print(f"Desconto: R${desconto:.2f}")

valor_a_pagar = preco_total - desconto
print(f"Valor a Pagar: R${valor_a_pagar:.2f}")
