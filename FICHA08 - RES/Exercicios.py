import csv
import matplotlib.pyplot as plt



filePath = './files/'
fileName = filePath+ "carros_usados.csv"



# CARROS POR MARCA
def chart1Plot(listaMarcas, nCarrosMarca):
    
    xpoints = (listaMarcas)
    ypoints = (nCarrosMarca)

    plt.plot(xpoints, ypoints, 
            marker = "D",
            ms = 10,
            mfc =  'red',
            linestyle = 'dotted')

    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Mercado Usados", fontdict= font1, loc = "center")   # loc = left, center, right
    plt.xlabel("Marcas Carros Usados")
    plt.ylabel("Nº de veículos")
    plt.ylim(0, 20000)

    plt.show()



# CARROS POR MARCA - GRAFICO CIRCULAR COM PERCENTAGENS
def chart2Pie(listaMarcas, nCarrosMarca):
    
    myExplode = []
    for i in range (len(listaMarcas)):
        myExplode.append(0.2)

    ypoints = (nCarrosMarca)

    plt.pie(ypoints, 
            labels=listaMarcas, 
            shadow=True,
            explode = myExplode,
            autopct='%1.1f%%')   # Atributo para evidenciar valores percentuais e respetiva formatação
          

    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Mercado Usados", fontdict= font1, loc = "center")   # loc = left, center, right
    plt.show()


# PREÇOS POR FUEL
def chart3Fuel(listaPetrol, listaDiesel, listaHybrid):
    
    xpoints = listaFuel
    
    precosPetrol= []
    for car in listaPetrol:
         precosPetrol.append(float(car['price']))

    precosDiesel= []
    for car in listaDiesel:
         precosDiesel.append(float(car['price']))

    precosHybrid= []
    for car in listaHybrid:
         precosHybrid.append(float(car['price']))


    plt.figure(figsize=(7,6))   # polegadas width , height
   
   
    ypoints= [min(precosPetrol), min(precosDiesel), min(precosHybrid)]
    plt.plot(xpoints, ypoints, 
             marker = 'D',
             ms = 15,
             mfc = 'red',
             linestyle = 'dotted',
             label = "Valor Mínimo",) 
          

    ypoints= [max(precosPetrol), max(precosDiesel), max(precosHybrid)]
    plt.plot(xpoints, ypoints,
             marker = 'p',
             ms = 15,
             mfc = 'blue',
             linestyle = 'dotted',
             label = "Valor Máximo",
             ) 
          
    ypoints= [sum(precosPetrol)/ len(precosPetrol), 
              sum(precosDiesel)/ len(precosDiesel),
              sum(precosHybrid)/len(precosHybrid) ]
    
    plt.plot(xpoints, ypoints,
             marker = 'o',
             ms = 15,
             mfc = 'green',
             linestyle = 'dotted',
             label = "Valor Médio",) 
    
    #plt.ylim(10000,150000)
    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Mercado Usados", fontdict= font1, loc = "center")   # loc = left, center, right
    plt.xlabel("Combustível")
    plt.ylabel("Preços")
    plt.legend(loc='upper right')
    plt.show()



def obterModelosPorMarca(marca):    #   Venda de carros por marca / modelo
    #  
    listaModelos= []
    nCarrosModelo = []

    #marcaChart = marca.lower()   # marca escolhida para o gráfico
    for linha in listaCarros:
        if linha['Make'].lower() != marca.lower():
            continue
        modelo = linha['model'].lower()
        if modelo == "": continue               # dados inválidos, ignorar
        if modelo not in listaModelos:
            listaModelos.append(modelo)
            nCarrosModelo.append(1)
        else:
            pos = listaModelos.index(modelo)
            nCarrosModelo[pos]+=1
    return listaModelos, nCarrosModelo




def chartPlot4(marca):    #   Venda de carros por marca / modelo
    #  
    listaTypeFuel= ['Petrol', 'Diesel', 'Hybrid']
    nCarrosMarca = [0, 0, 0]
    for linha in listaCarros:
        if linha['Make'].lower() != marca.lower():
            continue
        typeFuel = linha['TypeFuel'].lower()
        if typeFuel == "Petrol": 
            nCarrosMarca[0] += 1
        elif typeFuel ==  "Diesel":  
            nCarrosMarca[1] += 1
        elif typeFuel ==  "Hybrid":  
            nCarrosMarca[2] += 1



    xpoints = (nCarrosMarca)
    ypoints = (listaTypeFuel)

    plt.barh(xpoints, ypoints, 
            marker = "D",
            ms = 10,
            mfc =  'blue',
            linestyle = 'dotted')

    font1 = {'family':'serif','color':'blue','size':20}
    plt.title(f"Vendas da {marca}", fontdict= font1, loc = "center")   # loc = left, center, right
    plt.xlabel("Modelos de Carros")
    plt.ylabel("Nº de veículos")
    #plt.ylim(0, 20000)

    plt.show()




def chartPlot5(marca):   #   Venda de carros por marca / modelo - Gráfico de barras
    #  
    listaTypeFuel= ['Petrol', 'Diesel', 'Hybrid']
    nCarrosFuelType = [0, 0, 0]
    for linha in listaCarros:
        if linha['Make'].lower() != marca.lower():
            continue
        typeFuel = linha['fuelType']
        if typeFuel == "Petrol": 
            nCarrosFuelType[0] += 1
        elif typeFuel ==  "Diesel":  
            nCarrosFuelType[1] += 1
        elif typeFuel ==  "Hybrid":  
            nCarrosFuelType[2] += 1



    xpoints = (listaTypeFuel)
    ypoints = (nCarrosFuelType)

    plt.barh(xpoints, ypoints, 
            color = 'red',
            height = 0.4,
            )

    font1 = {'family':'serif','color':'blue','size':20}
    plt.title(f"Vendas da {marca}", fontdict= font1, loc = "center")   # loc = left, center, right
    plt.xlabel("Modelos de Carros")
    plt.ylabel("Nº de veículos")
    #plt.ylim(0, 20000)

    plt.show()







#---------------------------------------------

listaMarcas= []
nCarrosMarca = []
listaFuel = ['Petrol', 'Diesel', 'Hybrid']


with open(fileName, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    listaCarros = list(reader)

for linha in listaCarros:
        marca = linha['Make'].lower()
        if marca == "": continue                        # dados inválidos, ignorar
        if marca not in listaMarcas:
            listaMarcas.append(marca)
            nCarrosMarca.append(1)
        else:
            pos = listaMarcas.index(marca)
            nCarrosMarca[pos]+=1

# FILTRAR POR TIPO DE COMBUSTÍVEL
listaPetrol = [carro for carro in listaCarros if carro['fuelType']=='Petrol']
listaDiesel = [carro for carro in listaCarros if carro['fuelType']=='Diesel']
listaHybrid = [carro for carro in listaCarros if carro['fuelType']=='Hybrid']


# NESTA ALTURA tenho uma lista comm as  marcas de automóveis no ficheiro CSV             
#print(nCarrosMarca)

chart1Plot(listaMarcas, nCarrosMarca)
chart2Pie(listaMarcas, nCarrosMarca)
chart3Fuel(listaPetrol, listaDiesel, listaHybrid)
chartPlot4('audi')
chartPlot4('hyundai')

marca = input("MARCA: ")
chartPlot5(marca)

