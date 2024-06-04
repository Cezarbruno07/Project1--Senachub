#aula 03-06 tratamentos de erros try  e except else 

while True:
    try:
        cad= int(input("Digite \n1 para cadastro ou \n0 para \nencerrar = "))
    except:
        print("Valor Invalido")
    else:
        if(cad==1):
            nome=input("digite seu nome = ")
            try:
                rg=int(input("Digite seu rg ="))
            except:
                print("Digite um RG Valido")
                continue
            try:
                idade=int(input("Digite sua idade "))
            except:
                print("digite uma idade valida")
            print (f"\n{nome} \n{rg} \n{idade}")
        elif (cad==0):
            print("Saindo")
            break
        else:
            print("opção invalida")













