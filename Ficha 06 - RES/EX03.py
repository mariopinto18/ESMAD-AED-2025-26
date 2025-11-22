from PIL import Image
"""
Cria uma imagem de 240x240 pixels
"""
pathImages = "./images/"          # Opcional: caminho da pasta atual de imagens
width = 240
height= 240


newSize = (width, height) # Tuplo com largura (width) e altura (height) da imagem
image1 = Image.new(size=newSize, mode = "RGB", color= "white")  # Nova imagem

pixelMap= image1.load()             # "loads" the pixel para uma lista bidimensional
for col in range(image1.width):       # LARGURA
    for lin in range(image1.height):  # ALTURA
        if col <80:                     # primeiras 80 colunas  da largura (width) total da imagem
            pixelMap[col,lin] = (0, 0, 255)          # Azul
        elif col < 160:       
            pixelMap[col,lin] = (255, 255, 255)     # Branco
        else:
            pixelMap[col,lin] = (255, 0, 0)         # Vermelho

image1.show()                           # mostra a imagem
image1.save(pathImages+'bandeira.jpg')     # Grava imagem no ficheio pretendido