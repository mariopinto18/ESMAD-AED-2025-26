import csv
import numpy as np
import matplotlib.pyplot as plt



filePath = './files/'
fileName = filePath+ "films.csv"



def loadDataFilms():
    """
    Retorna os dados dos filmes e o header (nomes dos atributos)
    """
    with open(fileName, newline='', encoding='utf-8') as csvfile:
        filmsReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(filmsReader)  # Skip header
        filmsData = list(filmsReader)   

    return filmsData, header  



def showDatasetResume():
    """
    Mostra um resumo do dataset
    """
    print("\nNumber of films :", len(filmsData))
    print("\nDimension of films data: ", np.shape(filmsData)[0], "films")
    print("\nAtributes of dataset: ", np.shape(filmsData)[1], "attributes")
    print("\nAttributes names: ")
    for attr in header:
        print(" - ", attr)


def cleanDataset(filmsData):
    """
    Limita o dataset a 100 filmes e remove filmes com rating ou género vazio
    Retorna o dataset limpo
    """

    filmsData= filmsData[0:100]   # LIMITAR o número de filmes a 100 para melhor desempenho

    indexRating = header.index('rating')
    indexGenre = header.index('genre')

    filmsToRemove = []
    for film in filmsData:
        if film[indexRating] == '' or film[indexGenre] == '':
            filmsToRemove.append(film)

    for film in filmsToRemove:
        filmsData.remove(film)

    print("\nNumber of films after cleaning:", len(filmsData))
    return filmsData




def showFilmsByGenre():
    """
    calcula e mostra Nº e filmes por género através de:
    - Gráfico de barras 
    - Gráfico circular (pie chart)
    """
    genreItems = []              # LISTA de generos
    genreCount = []              # LISTA de contador de filmes para cada genero

    indexGenre = header.index('genre')
    
    for film in filmsData:      # Percorrer todos os filmes (agora 89 filmes)
        genresFilm = film[indexGenre].split(', ')  # Um filme pode ter vários géneros
    
        for genre in genresFilm:    # percorre todos os generos de UM DETERMINADO FILME 
            if genre in genreItems:
                pos=genreItems.index(genre) 
                genreCount[pos]+= 1
            else:
                genreItems.append(genre)
                genreCount.append(1)



    plt.figure(figsize=(12,6))  # width = 12 polegadas, hgeight= 6 polegadas  # Definir o tamanho da figura

    # Subplot 1 - bar chart by genre
    plt.subplot(1, 2, 1)
    
    plt.bar(genreItems, genreCount)
    plt.xlabel('Genre')
    plt.ylabel('Number of Films')
    plt.title('Number of Films by Genre')
    plt.xticks(rotation=45)
    plt.tight_layout()


    # subplot 2 - pie chart by genre
    plt.subplot(1, 2, 2)

    myExplode = []
    for i in range (len(genreItems)):
        myExplode.append(0.1)

    ypoints = (genreCount)
    plt.pie(ypoints, 
            labels=genreItems, 
            shadow=True,
            explode = myExplode,
            autopct='%1.1f%%')   # Atributo para evidenciar valores percentuais e respetiva formatação
          

    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Films by Genre", fontdict= font1, loc = "center")   # loc = left, center, right
   
    plt.show()




def showFilmsByRating():
    """
    Mostra uma análise dos filmes por rating: 
    -Nº filmes com rating >= 8.0 
    - Nº filmes com rating entre 7.0 e 7.9
    - Nº filmes com rating < 7.0
    """

    indexRating = header.index('rating')

    arrayFilms  = np.array(filmsData) 
    arrayFilms = arrayFilms[arrayFilms[:,indexRating]!='']   # Remover ratings vazios

   
    print(np.mean(arrayFilms[:,indexRating].astype(float)) )   # na coluna rating
    print(np.min(arrayFilms[:,indexRating].astype(float)) )    # na coluna rating
    print(np.max(arrayFilms[:,indexRating].astype(float)) )   # na coluna rating


    filter1 = arrayFilms[:,indexRating].astype(float) >= 8.0
    filter2 = (arrayFilms[:,indexRating].astype(float) >= 7.0)  & (arrayFilms[:,indexRating].astype(float) < 8.0)
    filter3 = arrayFilms[:,indexRating].astype(float) < 7.0


    ratingItems = ['8.0 - 9.0', '7.0 - 7.9', '< 7.0']    
    ratingCount = [np.sum(filter1), np.sum(filter2), np.sum(filter3)]

   # Visualização
    plt.bar(ratingItems, ratingCount, color='red')
    plt.xlabel('Rating intervals')
    plt.ylabel('Number of Films')
    plt.title('Number of Films by Rating')
    plt.tight_layout()
    plt.show()




def showTopRating(top):
    """
    Determinar e mostrar os top filmes por rating
    """
    
    indexRating = header.index('rating')   # posição do atributo rating no cabeçalho

    arrayFilms  = np.array(filmsData)       # converter a lista filmsdata num array
 
    sortedFilms = arrayFilms[arrayFilms[:,indexRating].astype(float).argsort()[::-1]]  # Ordenar por rating decrescente   
    
    topFilms = sortedFilms[0:top]
    print("\n\t\t\tTop", top, "films by rating:\n")
    for film in topFilms:
        while len(film[1]) < 50:
            film[1]+= ' '
        print(" - ", film[1], " \t Rating: ", film[indexRating])
   
    




#---- INICIO DO PROGRAMA 
filmsData, header = loadDataFilms()
showDatasetResume()
filmsData = cleanDataset(filmsData)
 
showFilmsByGenre()
#showFilmsByRating()

top=10
#showTopRating(top)

