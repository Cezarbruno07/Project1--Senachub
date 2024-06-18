def data(data):
    if data [3:5]== "01":
        print(f"{data[0:2]} de janeiro de {data[6:]}")
        
data("01/01/2024")


meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]


data = input("informe a data (dd/mm/aaaa): ")

print (data.split("/")[0],"de",meses[(int(data.split("/")[1])-1)],"de",data.split("/")[2])
 