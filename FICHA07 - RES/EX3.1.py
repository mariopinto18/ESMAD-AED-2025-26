import csv
import matplotlib.pyplot as plt


"""
V1: Obter preço máximo, mínimo e média por marca 
"""

filePath = './files/'
fileName = filePath+ "carros_usados.csv"

marca = input("Qual a marca que pretende analisar? ")

listaCarrosMarca = []   # conterá APENAS os preços dos carros da marca

with open(fileName, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for linha in reader:    # cada linha do ficheiro
        marcaCarro = linha['Make'].lower()
        if marcaCarro != marca: continue 
        if marcaCarro == "": continue
        preco = float(linha['price'])
        
        listaCarrosMarca.append(preco)

if listaCarrosMarca == []:
    print(f"Não foram encontrados carros da marca {marca}")
else:
    print(f"Marca: {marca}")
    print(f"  Mínimo: {min(listaCarrosMarca)}")
    print(f"  Máximo: {max(listaCarrosMarca)}")
    print(f"  Médio : {sum(listaCarrosMarca)/len(listaCarrosMarca):.2f}")
    
  

# gráfico
xpoints= []
for i in range (len(listaCarrosMarca)):
    xpoints.append(i) 
ypoints = ([listaCarrosMarca])

plt.scatter( xpoints, ypoints, 
            color = "red")
 
font1 = {'family':'serif','color':'blue','size':20}
plt.title(f"Mercado de Usados {marca.upper()}", fontdict= font1, loc = "center")   # loc = left, center, right

labelX = "Carros " + marca 
plt.xlabel(labelX)
plt.ylabel("Preço de Venda")

plt.show()


