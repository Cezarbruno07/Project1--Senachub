def cadastro():
    name = input("qualseu nome :")
    age= int(input("qual sua idade :"))
    return name,age
print("Iniciando o cadastro ...")
name,idade= cadastro()
print("Cadastro realizado com sucesso")
print("Seu nome é ",name,"voce tem",idade,"anos de idade")
                