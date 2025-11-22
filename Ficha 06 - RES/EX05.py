from PIL import Image
"""
Criar imagem com uma moldura superior e inferior de 20 pixels, azul
""" 
pathImages = "./images/"          # Opcional: caminho da pasta atual de imagens
width = 240
height= 240
corMoldura = (255,0,255)    #MAGENTA

def imageMoldura(imagem1):
    pixelMap = imagem1.load()                  # load de pixel data (lista bidimensional)

    for col in range(imagem1.width):               # largura
        for lin in range(imagem1.height):          #altura
            if col <20 or col >imagem1.width-20:
                pixelMap[col,lin] = corMoldura     
            if lin <20 or lin > imagem1.height-20:   
                pixelMap[col,lin] = corMoldura

        if col > imagem1.width/2-5 and col < imagem1.width/2 +5:
            pixelMap[col,lin] = corMoldura
    return imagem1


# EX05
imagem1 = Image.open(pathImages+'img1.jpg')
image1= imageMoldura(imagem1)
imagem1.show()
imagem1.save(pathImages+'img1Moldura.jpg')