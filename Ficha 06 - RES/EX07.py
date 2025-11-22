from PIL import Image
"""
Criar imagem com uma moldura superior e inferior de 20 pixels, azul
""" 
pathImages = "./images/"                   # caminho da pasta atual de imagens
imagem1 = Image.open(pathImages+'img1.jpg')
pixelMap = imagem1.load()                  # load de pixel data (lista bidimensional)

corMoldura = (0, 0 ,255)    # moldura de cor Azul
espessura = 10              # espessura da moldura em pixels

for i in range(imagem1.width):                   # largura
    for j in range(imagem1.height):              #altura
        if i <espessura or i >imagem1.width-espessura:    # primeiro e ultimos 10 pixels, em largura (esquerda e direita)
             pixelMap[i,j] = corMoldura           
          
        if j <espessura or j > imagem1.height-espessura:   # primeiros e ultimso 10 pixels em altura ( cima e baixo)
            pixelMap[i,j] = corMoldura           # cor
        
        if i > imagem1.width/2- espessura/2 and i < imagem1.width/2 + espessura/2:
            pixelMap[i,j] = corMoldura          # cor
         
        if j > imagem1.height/2- espessura/2 and j < imagem1.height/2 + espessura/2:
            pixelMap[i,j] = corMoldura          # cor
        
imagem1.show()
imagem1.save(pathImages+'img1Moldura.jpg')