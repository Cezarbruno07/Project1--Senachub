
#Cadastro de alunos escolinha Conda 
import sqlite3

banco = sqlite3.connect('cadastrodealunos.db')#conexao do banco

cursor = banco.cursor()

#cursor.execute("CREAT TABLE alunos(Nome text,idade integer,email text,telefone interger)")

cursor.execute("INSERT INTO alunos VALUES('Thiago',41,'thiago_123@gmail.com''6799215548')")

banco.commit('cadastrodealunos.db')

""" cursor.execute("SELECT *FROM alunos")

print(cursor.fetchall()) """
