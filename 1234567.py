
valor_lido = input("digite um valor: ")
digite um valor: 10

type(valor_lido)  # deve-se notar que o valor lido é SEMPRE do tipo string
<class 'str'>
valor_lido + 10  # para trabalhar com esse valor, é preciso converter para o tipo correto
Traceback (most recent call last):
    ...
TypeError: must be str, not int

valor_lido = int(input("digite um valor inteiro: "))
digite um valor inteiro: 10

type(valor_lido)
<class 'int'>

valor_lido + 10
20

valor_lido = float(input("digite um valor decimal: "))
digite um valor decimal: 1.5

valor_lido - 1
0.5
frase = input()
Rosas são vermelhas, violetas são azuis, girassóis são legais.
frase
'Rosas são vermelhas, violetas são azuis, girassóis são legais.'

<nome lido> roubou pão na cassa do <nome2 lido>!
<nome2 lido> ficou triste e com fome,
porque o bandejão estava fechado.