import random

# função geradora de passwords
def generatePassword(userName):
    """
    Gera e devolve uma password, baseada no userName\n
    Args: userName string
    Returns: string
    """
    if userName.find(" ")!= -1:    # username NÂO PODE TER espaços
        return "username Inválido!"
    
    password = ""         # password é constituída pelas posições PARES, seguidas de random
    for i in range(1, len(userName), 2):       
        password+= userName[i] + str(random.randint(1,9))     
    # no final a password termina com o nº caracteres do userName
    password+= str(len(userName))
    return password


# EX 07
userName = input("Username: ")
passwd= generatePassword(userName)
print("\npassword:{0}" .format(passwd))

