def printCharLine(texto, numCar):
    """
    Recebe um texto e imprime numCar caracteres por linha\n
    Args: texto: string, 
          numCar: int
    """
    pos=0                                  # pos do texto onde começo a imprimir
    while (pos+numCar < len(texto)):       # Enq. tiver numCar para imprimir
        print(texto[pos: pos+numCar])
        pos+= numCar
    print(texto[pos:])                    # Imprime os últimos caracteres do texto 

texto = input("Texto:")
numCar = int(input("\nNº caracteres a imprimir por linha:"))
printCharLine(texto, numCar)

