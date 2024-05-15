
#Cadastro de alunos escolinha Conda 
import sqlite3
<<<<<<< Updated upstream

banco = sqlite3.connect('cadastrodealunos.db')#conexao do banco

cursor = banco.cursor()

#cursor.execute("CREAT TABLE alunos(Nome text,idade integer,email text,telefone interger)")
=======
banco = sqlite3.connect('cadastrodealuno.db')
cursor = banco.cursor()

#cursor.execute("CREAT TABLE Alunos(Nome text,idade integer,email text)")
cursor.execute("INSERT INTO alunos VALUES(,Maria,40,'Maria_123@gmail.com')")
banco.commit('cadastrodealuno.db')
cursor.execute("SELECT *FROM pessoas")
>>>>>>> Stashed changes

cursor.execute("INSERT INTO alunos VALUES('Thiago',41,'thiago_123@gmail.com''6799215548')")

<<<<<<< Updated upstream
banco.commit('cadastrodealunos.db')
=======
 na= str(input("Nome do aluno = "))
ia=int(input("Idade do aluno = "))
nr=str(input("Nome do Responsalvel = "))
>>>>>>> Stashed changes

""" cursor.execute("SELECT *FROM alunos")

<<<<<<< Updated upstream
print(cursor.fetchall()) """
=======

print ('Nome do aluno = ',na)
print ('Idade do aluno = ',ia) 
print ('Nome do responsavel =',nr) 
>>>>>>> Stashed changes
