import os


def writeText(text):
    """
    recebe um texto e guarda em ficheiro binário
    """
    with open(fileName, 'wb') as file:
        file.write(text.encode('utf-32'))
    file.close()



def readText():
    """
    Lê ficheiro binário e devolve o conteúdo, convertido para string
    """
    with open(fileName, 'rb') as file:
        text = file.read().decode('utf-32')
    file.close()
    return text

# EX02 -----------------------------------------
pasta    = "files"
fileName = "./files/texto.bin"

# se a pasta files não existe, cria a pasta
if not os.path.exists(pasta):   # SE a sub-pasta files não existir
    os.mkdir(pasta)   

texto = input("Texto para escrever em ficheiro binário:")
writeText(texto)


texto = readText()
print(f"\nleitura do ficheiro binário: {texto}")