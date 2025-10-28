
def countText(texto):
    """
    Recebe um texto e imprime o nº de caracteres, 
    de vogais e de espaços do texto\n
    Args: string, texto inserido
    """
    vogais=0
    comp = len(texto)           # nº de caracteres do texto
    espacos= texto.count(" ")    # conta nº de espaços do texto

    listaVogais = 'aeiou'
    for i in range(0,comp):     # percorre o texto, caracter a caracter, contando as vogais
        if texto[i].lower() in listaVogais:
            vogais+=1

    print("Nº de caracteres:", len(texto))
    print("Nº de vogais    :", vogais)
    print("Nº de espaços   :", espacos)


# EX02
texto = input("Indique um texto:")
countText(texto)

