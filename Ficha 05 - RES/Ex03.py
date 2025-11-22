import os

# entrada de veiculos no parque: ocupa o primeiro lugar vago (com 0)
def entrada_parque():

    for i in range(filas):
        for j in range(lugares):
            if parque [i][j] ==0:
                parque[i][j] = 1
                print("\n\n\tlugar ocupado: Fila {0}, Lugar {1}" .format(i+1, j+1))
                input()
                return
    print("\tO parque está completo! :(")
    input()


def saida_parque():
# Saida de carros do parque: indicando a fila e lugar do carro
    try:
        saidaFila = int(input("\n\n\tFila : "))
        saidaLugar = int(input("\tLugar:"))
        if saidaFila > filas:
            raise ValueError()
        if saidaLugar > lugares:
            raise ValueError()
    except:
        print("\tA fila ou lugar indicados não são válidos")
    else:
        if parque[saidaFila-1][saidaLugar-1] == 0:
            print("\tO lugar indicado não está ocupado!")
        else:
            parque[saidaFila-1][saidaLugar-1] =0
            print("\to lugar foi desocupado!")
    input()


def estado_parque():
# Função de conta o nº de lugares livres e ocupados do parque
    cont_livres =0
    cont_ocup = 0
    for i in range(filas):
        for j in range(lugares):
            if (parque[i][j]== 0):
                cont_livres+=1
            else:
                cont_ocup+=1
    print("\n\n\t\tESTADO DO PARQUE")
    print("\tNº lugares livres  : {0}" .format(cont_livres))
    print("\tNº lugares ocupados: {0}" .format(cont_ocup))
    input()
    


# EX03 - PARKING CAR
filas = 3
lugares = 5
#parque = cria_lista()   ## lista do parque por ocupar!
parque = [[0] * 5, 
          [0] * 5,
          [0] * 5]
print(parque)


# Construção do Menu do programa
op = " "
while op != "0":
    os.system("cls")
    print("\t\tMENU")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Estado do Parque")
    print("0 - Sair")
    op = input("Escolha uma das opções: ")
    if op == "1":
        entrada_parque()
    elif op == "2":
         saida_parque()
    elif op == "3":
        estado_parque()
   