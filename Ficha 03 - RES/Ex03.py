# Função que recebe um texto e verifica se é capicua ou não
def capicua(texto):
    """
    Recebe um texto e devolve um valor booleano: 
    True se for capicua. False caso não seja
    Args: string, texto aavaliar\n
    Returns: booleano, True ou False
    """
    if texto == texto[::-1]:
       return True
    else:
        return False

# EX 03
#--------------------------------
texto = input("\tInsira um texto: ").lower()
if capicua(texto) == True:
    print("\t{0} é capicua" .format(texto))
else:
    print("\t{0} não é capicua" .format(texto))


