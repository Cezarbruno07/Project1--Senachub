def Con_digito(n):
    return len(str(n))
def exibe():
    n = int(input('Digite uma Sequencia de numeros = '))
    print(Con_digito(n), ' Dígitos')
    
while True:
    exibe()