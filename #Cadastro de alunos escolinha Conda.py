
#Cadastro de alunos escolinha Conda 
import sqlite3

banco = sqlite3.connect('Cadastrodealunos.db')

cursor = banco.cursor()

cursor.execute("CREAT TABLE alunos(Nome text,idade integer,email text)")

cursor.execute("INSERT INTO alunos VALUES('bruno',40,'bruno_123@gmail.com)")

banco.commit('cadastrodealunos.db')

cursor.execute("SELECT *FROM pessoas")

print(cursor.fetchall())

