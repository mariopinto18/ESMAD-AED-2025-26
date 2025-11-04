import random

def generateEuromillionKeys():
    """
    generates euromillions keys randomly 
    returns a list of numbers and a list os stars
    """
    chave = []
    estrelas = []
   
    # Gerar 5 números
    i=0
    while i <5:                          
        numero = random.randint(1,50)    
        if numero not in chave:          # se nº gerado NAO EXISTE na lista
            chave.append(numero)         # acrescenta à lista
            i+=1
    # Gerar 2 estrelas
    i=0
    while i <2:                          
        numero = random.randint(1,12)    
        if numero not in estrelas:       # se nº gerado NAO EXISTE na lista
            estrelas.append(numero)      # acrescenta à lista
            i+=1

    chave.sort()
    estrelas.sort()
    return chave, estrelas


#------- VERSÂO MAIS COMPACTA, RECORRENDO AO MÉTODO sample 
def generateEuromillionKeysV2():
    """
    generates euromillions keys randomly 
    returns a list of numbers and a list os stars
    """
    chave = random.sample(range(1,51), 5)
    estrelas = random.sample(range(1,13), 2)
    chave.sort()
    estrelas.sort()
    return chave, estrelas




# Inicio da execução do programa
op = "S"
while op.upper() == "S":
    chave, estrelas = generateEuromillionKeys()
    print("\n Chave do Euromilhões: {} \t Estrelas: {}" .format(chave, estrelas))
    op = input("\nDeseja gerar nova chave(S/N)?:")
  



