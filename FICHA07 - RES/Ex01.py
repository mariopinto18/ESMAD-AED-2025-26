import os

listaContinentes = ["Europa", "America", "Africa", "Asia", "Oceania"]


def lerFicheiro():
    """
    Devolve o conteúdo existente em ficheiro
    """
    listaPaises = []
    if os.path.exists(ficheiro) == True:
        fPaises = open(ficheiro, "r", encoding="utf-8")
        listaPaises = fPaises.readlines()
        fPaises.close()
    return listaPaises


def paisExiste(pais):
    """ 
    Função que verifica se o pais já existe no ficheiro. 
    Devolve devolve True se existir, caso contrário False
    """
    try:
        fPaises = open(ficheiro, "r", encoding="utf-8")
        listaPaises = fPaises.readlines()
    except Exception as e:
        print(f'Ocorreu um erro na leitura do ficheiro: {e}')
        input()
        return True
    finally:
        fPaises.close()

    for linha in listaPaises:      # percorre toda a lista paises
        if linha.split(';')[0] == pais:   # CASO encontre o país no FICHEIRO
            return True
    return False  # se chegou ao fim do for e nunca devolveu True, é pq o pais não existe no ficheiro


def guardarFicheiro(pais, continente):
    """
    Acrescenta ao ficheiro o país e continente passados como parâmetros 
    """ 
    linha = pais + ";" + continente + "\n"
    f = open(ficheiro, "a", encoding="utf-8")
    f.write(linha)
    f.close()




def inserePais():
    """ 
    Implementar a opção 1, solicitar pais e continente  
    e guardar em ficheiro
    """
    os.system("cls")
    print("\n\n\n\n")
    pais = input("\t\tPaís       : ")
    print('\n')

    continente = input("\t\tContinente : ")
    if continente not in listaContinentes:      # Verifica se continente é válido
        print("\n\nO Continente {:s} não existe! Prime <enter> para continuar..." .format(continente))
        input()
        return
    if paisExiste(pais) == True:       # verifica se pais já existe em ficheiro
        print("\n\nO país {:s} já existe no ficheiro! Prime <enter> para continuar..." .format(pais))
        input()
        return
    guardarFicheiro(pais, continente)   # acrescenta ao ficheiro paises.txt



def cabecalho():
    os.system("cls")
    print()
    print()
    print("\t\t    País     \t Continente")
    print("\t\t------------------------------------------")


def consultaPaises():
    os.system("cls")
    cabecalho()
    pagina=1
    lin = 1
   
    listaPaises = lerFicheiro()
    for linha in listaPaises:
        if lin == 11:
            input("Pág. {0}. Prima <enter> para continuar" .format(pagina))
            pagina+=1
            lin=1
            cabecalho()       
        pais = linha.split(';')[0]
        continente = linha.split(';')[1]
        if len(pais) < 6:
            pais+= "\t"
        print("\t\t", pais, "\t", continente)
        lin+=1
    input()




def consultaContinente():
    """
    Consulta a lista de países por continente
    """
    os.system("cls")
    continente = input("\n\n\t\tContinente: ")
    cabecalho()
    pagina=1
    lin = 1
 
    listaPaises = lerFicheiro()
   
    continente = continente + "\n"
    for linha in listaPaises:
        if lin == 11:
            input("Pág. {0}. Prima <enter> para continuar" .format(pagina))
            pagina+=1
            lin=1
            cabecalho("Continente:" + continente)     
        if continente != linha.split(';')[1]:    # se não for o continente pedido, salta prox. iteração
            continue
        pais = linha.split(';')[0]              # obter nome pais
        if len(pais) < 6:
            pais+= "\t"
        print("\t\t", pais, "\t", continente)
        lin+=1
    input()


def consulta():
    pass

 
# Variáveis globais do programa, que definem o nome da pasta e do ficheiro (path incluida)
pasta = "files"
ficheiro = "./files/paises.txt"

# se a pasta files não existe, cria a pasta
if not os.path.exists(pasta):
    os.mkdir(pasta)

opcao = "1"
while opcao != "0":
    os.system("cls")
    print("\n\n\tMENU")
    print("\t1 - Inserir Países")
    print("\t2 - Consulta Países")
    print("\t3 - Consulta por Continente")
    print("\t4 - Consulta nº Países")
    print("\t0 - Sair")
    opcao = input("\t\t opção: ")
    match opcao:
        case "1": inserePais()
        case "2": consultaPaises()
        case "3": consultaContinente()
        case "4": consulta()