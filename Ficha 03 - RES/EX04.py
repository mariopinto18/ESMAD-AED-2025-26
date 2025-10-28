# Função que substitui 2 ou mais espaços por um único espaço
def removeSpaces(texto):
    """
    A função recebe uma string 
    e substitui sequências de 2 ou mais espaços por um único espaço\n
    Args: string, texto
    """
    
    while texto.find("  ")!= -1 :          # Enquanto encontrar sequências de 2 espaços
        texto = texto.replace("  ", " ")   # substituir 2 espaços por 1
    print("\nTexto:",texto)


    """  VERSÃO 2 DA MESMA FUNÇÃO"""
    textoResult=""
    palavras = texto.split(" ")
    for item  in palavras:
        if item != '':
            textoResult+= item + " "
    print(textoResult)



# EX 04
texto = input("Insira um Texto:") 
removeSpaces(texto)

