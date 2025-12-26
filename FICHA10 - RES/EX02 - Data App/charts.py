import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os



"""
chart to show films by genre
"""

def filmsByGenreChart(header, filmsData):
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


    chart1Path = os.path.join("static", "images", "plot1.png")
    plt.figure()

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

   
    plt.tight_layout()
    plt.savefig(chart1Path)
    plt.close()
    return chart1Path





"""
chart to show films by rating: intervals
- Nº films with rating >= 8.0   
- Nº films with rating between 7.0 and 7.9
- Nº films with rating < 7.0
"""
def filmsByRatingChart(header, filmsData):

    indexRating = header.index('rating')

    arrayFilms  = np.array(filmsData) 

    filter1 = arrayFilms[:,indexRating].astype(float) >= 8.0
    filter2 = (arrayFilms[:,indexRating].astype(float) >= 7.0)  & (arrayFilms[:,indexRating].astype(float) < 8.0)
    filter3 = arrayFilms[:,indexRating].astype(float) < 7.0


    ratingItems = ['8.0 - 9.0', '7.0 - 7.9', '< 7.0']    
    ratingCount = [np.sum(filter1), np.sum(filter2), np.sum(filter3)]
    
    chart2Path = os.path.join("static", "images", "plot2.png")
    plt.figure()

    plt.bar(ratingItems, ratingCount, color='red')
    plt.xlabel('Rating intervals')
    plt.ylabel('Number of Films')
    font1 = {'family':'serif','color':'blue','size':20}

    plt.title('Number of Films by Rating', fontdict= font1, loc = "center")   # loc = left, center, right
  
    plt.tight_layout()
    plt.savefig(chart2Path)
    plt.close()
    return chart2Path
