import sqlite3
nome=str(input("Digite seu nome = "))
idade=int(input("Qual idade = "))
email=bool(input("Digite seu email = "))
telefone=int(input("Telefone = "))

aluno=aluno=+1

banco = sqlite3.connect('cadastrodealunos.db')#conexao do banco

cursor = banco.cursor()

banco = VALUES = ('Idade',nome,'Idade',idade,'Email',email,'Telefone',telefone,)

banco.commit('cadastrodealunos.db')

#cursor.execute("SELECT *FROM alunos")

#print(cursor.fetchall()) 
