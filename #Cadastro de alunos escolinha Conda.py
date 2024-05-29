import sqlite3
<<<<<<< Updated upstream
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
=======
banco = sqlite3.connect('Cadastro_de_alunos.db')
""" cursor = banco.cursor()

#cursor.execute("CREAT TABLE Alunos(Nome text,idade integer,email text)")
cursor.execute("INSERT INTO alunos VALUES('Maria',40,'Maria_123@gmail.com')")


cursor.execute("INSERT INTO  pessoas")

banco.commit() """



>>>>>>> Stashed changes
