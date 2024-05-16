""" def saudacao():
nome = input(str("Qual seu nome?")) """
nome=input('digite seu Nome ')
def saudacao():
  if(nome[-1]=='a' or nome[-1]=='e'):
    print(f"Bom dia mulher ! Teu nome é {nome}, prenda!")
  else:
    print(f"Bom dia homem, guri! Teu nome é {nome}, galo véio!")