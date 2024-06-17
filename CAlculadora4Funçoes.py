def calc():
    a=int(input(" Digite a operação matematica desejada\n1 (somar)\n2 (Subtrair)\n3 (dividir)\n4 (multiplicar)\n\n"))
    
    
    if( a!=1 and a!=2 and a!=3 and a!=4):
        print("valor não reconhecido")
        
    

    elif(a==1):
        b=int(input("Digite o primeiro valor : \n"))
        c=int(input("Digite segundo Valor : \n"))
        print(b+c)
    elif(a==2):
        b=int(input("Digite o primeiro valor : \n"))
        c=int(input("Digite segundo Valor : \n"))
        print(b-c)
    elif(a==3):
        b=int(input("Digite o primeiro valor : \n"))
        c=int(input("Digite segundo Valor : \n"))
        print(b/c)
    elif(a==4):
        b=int(input("Digite o primeiro valor : \n"))
        c=int(input("Digite segundo Valor : \n"))
        print(b*c)
        

calc()