from PIL import Image
import random

"""
Cria uma imagem de 400x400 pixels
"""
pathImages = "./images/"          # Opcional: caminho da pasta atual de imagens
width = 400
height= 400

def ImageArt():
    """
    Gera uma nova imagem pixelada com RGB gerado aleatoriamente
    entre 0-255
    """
    imageSize = (width, height)
    image1 = Image.new(size = imageSize, mode="RGB")
    pixelMap = image1.load()
    # Iterar todos os pixels da imagem, gerando um tuplo RGB 
    # para cada pixel 
    for i in range(width):
        for j in range(height):
            r = random.randint(0,255)   
            g = random.randint(0,255)
            b = random.randint(0,255)
            pixelMap[i,j] = (r,g,b)
    image1.show()
    image1.save(pathImages+'imageArt.jpg')


ImageArt()