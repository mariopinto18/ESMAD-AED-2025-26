from PIL import Image
import random

pathImages = "./images/"
width = 250
height= 250

def ImageGradient():
    """
   The image should represent a smooth gradient from blue to red 
   (no green)
    """
    imageSize = (width, height)
    image1 = Image.new(size = imageSize, mode="RGB")
    pixelMap = image1.load()

    for col in range(width):        # "colunas" de pixels da imagem
        for lin in range(height):   # "linhas"  de pixels da imagem
            b= 255 - col
            r = col
            g= 0
            pixelMap[col,lin] = (r,g,b)
    image1.show()
    image1.save(pathImages+'Gradient.jpg')


ImageGradient()