try:
    a = int(input("digite uma plavra = "))

except ValueError:
    print ("Digite apenas numeros")

except:
    print("Erro desconhecido")
else:
    print("Deu certo")

finally:
    print("Final do algoritimo")
