def standardName(nome):
    """
    function receives a string text and returns the firt name, last name and 
    initials of middle names\n
    Args:  nome - string
    Returns: string
    """
    if nome.count(" ") ==  0:
        return "nome inválido, deve ter pelo menos 1 espaço"
    listNomes = nome.split(' ')
    # primeiro nome
    nomeAbrev= listNomes[0] + " "

    # Iniciais dos nomes intermédios
    for i in range (1, len(listNomes)-1): 
        nomeIntermedio = listNomes[i]
        nomeAbrev+= nomeIntermedio[0] + ". " 
    
    # último sobrenome
    nomeAbrev+= listNomes[-1]
    return nomeAbrev


#EX 06
nome = input("Indique um nome:")
print(standardName(nome))
