import csv
import matplotlib.pyplot as plt

filePath = './files/'
fileName = filePath+ "carros_usados.csv"


listaDeMarcas= []       #lista de marcas existentes no CSV
listaCarrosMarca = []   # lista com preços dos carros de cada marca

with open(fileName, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for linha in reader:
        marca = linha["Make"].lower()
        preco = float(linha["price"])
        if marca == "": continue
        if marca not in listaDeMarcas:
            listaDeMarcas.append(marca)        # adiciona à lista de marcas
            listaCarrosMarca.append([preco])   # cria lista com preços para a marca
        else:
            pos = listaDeMarcas.index(marca)
            listaCarrosMarca[pos].append(preco)


precoMedioMarca= [] # lista com preço médio de cada marca
for linha in listaCarrosMarca:
    print(f"Marca: {marca}")
    print(f"  Mínimo: {min(linha)}")
    print(f"  Máximo: {max(linha)}")
    print(f"  Médio : {sum(linha)/len(linha):.2f}")
    
    precoMedioMarca.append(sum(linha)/len(linha))
    
  

# gráfico
xpoints = (listaDeMarcas)   # MARCAS
ypoints = (precoMedioMarca) # PRECO MEDIA DE CADA MARCA

plt.plot(xpoints, ypoints, 
         marker = "D",
         ms = 10,
         mfc =  'red',
         linestyle = 'dotted')

font1 = {'family':'serif','color':'blue','size':20}
plt.title("Amostra do Mercado Usados", fontdict= font1, loc = "center")   # loc = left, center, right
plt.xlabel("Marcas Carros Usados")
plt.ylabel("Preço Médio de Venda")
plt.ylim(5000, 25000)
plt.show()



