#reverseWords - recebe um texto e inverte a ordem das palavras
def reverseWords(text):
    """
    Recebe uma string (texto) 
    e devolve o mesmo texto, com as palavras por ordem inversa
    Args: string
    Returns: string
    """
def reverseWords(text):
    newText=""
    listWords = text.split(' ')     # lista de palavras do texto
    listWords= listWords[::-1]      # Inverte a ordem da lista de palavras    
    for word in listWords:          # Iterar a lista de palavras
        newText+= " "+ word         # concatenar as diversas posições da lista 
    return newText.strip()


# EX 08
text = input("Texto:")
print(reverseWords(text))

