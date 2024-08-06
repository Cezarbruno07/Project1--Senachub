""" Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual  

operação ele deseja realizar.  

  

O resultado da operação deve ser acompanhado de uma  

frase que diga se o número é:  

    par ou ímpar;  

    positivo ou negativo;  

    inteiro ou decimal.   """
    
n1=
n2=int(input("Digite o segundo numero: "))

op=int(input("Qual operaçao deseja realizar: \n1-adicao \n2-subtração \n3-Multiplicação \n4-Divisão \n"))
if op == 1:
    r=n1+n2
    print(f"Resultado da operação é {r}")
    if r > 0 :
        print("Positivo")
    else:
        print("Negativo") 
    if r%2 == 0:
        print("Par")
    else: 
        print("Impar")    
    if r%1 == 0:
        print ("inteiro")
    else :
        print('decimal')    
    
 
    
elif op == 2:
    r=n1-n2
    print(f"Resultado da operação é {r}")
    if r > 0 :
        print("Positivo")
    else:
        print("Negativo") 
    if r%2 == 0:
        print("Par")
    else: 
        print("Impar")  
    if r%1 == 0:
        print ("inteiro")
    else :
        print('decimal')        
        
elif op == 3:
    r=n1*n2
    print(f"Resultado da operação é {r}")
    if r > 0 :
        print("Positivo")
    else:
        print("Negativo") 
    if r%2 == 0:
        print("Par")
    else: 
        print("Impar")  
    if r%1 == 0:
        print ("inteiro")
        
    else :
        print('decimal') 
               
elif op == 4:
    r=n1/n2
    print(f"Resultado da operação é {r}")
    if r > 0 :
        print("Positivo")
    else:
        print("Negativo") 
    if r%2 == 0:
        print("Par")
    else: 
        print("Impar")  
    if r%1 == 0:
        print ("inteiro")
    else :
        print('decimal')        