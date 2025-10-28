# função que recebe um texto e devolve o primeiro e último nome 
def shortName(nome):
    """
    recebe um nome e devolve-o no formato shortName: primeiro e último sobrenome\n
    Args: string
    Returns: string
    """
    nomeAbrev = ""
    pos = nome.find(" ")                    # procura o 1º espaço
    if pos != -1:
        primeiroNome = nome[:pos]           # obtém o 1º nome (até ao espaço)
        pos = nome.rfind(" ")               # procura o último espaço
        if pos != -1:
            ultimoNome = nome[pos+1:]       # Obtém o último nome (do espaço até ao fim)
            nomeAbrev = primeiroNome+ " " + ultimoNome
            return nomeAbrev
    return "nome inválido"                  # no caso de não ter feito o return  na linha anterior


#----- VERSÃO 2 DA MESMA FUNÇÃO
def shortNameV2(nome):
    if nome.count(" ") ==  0:
        return "nome inválido, deve ter pelo menos 1 espaço"
    nomeAbrev=""
    listNomes = nome.split(' ')
    nomeAbrev= listNomes[0] + " " + listNomes[-1]
    return nomeAbrev


# EX 05
nome = input("Nome:")
print(shortNameV2(nome))


