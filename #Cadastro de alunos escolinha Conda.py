
#Cadastro de alunos escolinha Conda 
import sqlite3
banco = sqlite3.connect('Cadastrodealunos.db')
cursor = banco.cursor()

#cursor.execute("CREAT TABLE Alunos(Nome text,idade integer,email text)")
cursor.execute("INSERT INTO alunos VALUES(,Maria,40,'Maria_123@gmail.com')")
banco.commit()
cursor.execute("SELECT *FROM pessoas")

print(cursor.fetchall())

""" na= str(input("Nome do aluno = "))
ia=int(input("Idade do aluno = "))
nr=str(input("Nome do Responsalvel = "))



print ('Nome do aluno = ',na)
print ('Idade do aluno = ',ia) 
print ('Nome do responsavel =',nr) """ 