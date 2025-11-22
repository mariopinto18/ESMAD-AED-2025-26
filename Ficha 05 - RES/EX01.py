"""
Implement a program that allows you to generate a two-dimensional 3x3 list, that is, a matrix with 3 rows and 3 columns.
 the list with random integer values between 0 and 9;
 a showTable() function that displays the generated table;
 a verifyTable() function that checks and prints which row, column or diag-onal has the largest sum.
"""

import random

def showTable():
    print('\n Tabela Gerada aleatóriamente')
    for linha in matriz:        # Iterar linhas da matriz (sub-listas)
        print('\t', end = "")
        for coluna in linha:    # Iterar posições dentro de cada sub-listas
            print('{:g}' .format(coluna), end="  ")
        print('\n')             # no final de cada linha da tabela
    


def verifyTable():
    for i in range(3):              # 3 linhas da matriz / tabela
        print(f'Linha {i+1}:', sum(matriz[i]))

    listaSomasColunas= [0] * 3      # equivalente a listaSomasLinhas = [0, 0, 0]  
    for col in  range(3):
        for lin in range(3):
            listaSomasColunas[col]+= matriz[lin][col]
    print('Soma das colunas da tabela', listaSomasColunas)   



# EX01
matriz= []
lin = 3
col = 3
for i in range(lin):        # 3 linhas 
    matriz.append([])       # append de sub-lista vazia
    for j in range(col):      # preencher a sublista com valores aleatórios
        matriz[i].append(random.randint(0,9))

showTable()
verifyTable()
