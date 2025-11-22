"""
Implement a program that allows you to record and analyze rainfall indices in four cities
(Braga, Porto, Lisbon) over 6 months (from January to June).
"""
import os
import random

cidades = ['Braga', 'Porto', 'Lisboa']
meses = ['Janeiro  ', 'Fevereiro', 'Março    ', 'Abril    ', 'Maio     ', 'Junho    ']

ncidades = 3        # 3 cidades
nmeses=6            # 6 meses




def showData(rainfall):
    os.system('cls')                    # 'cls' - clear screen
    print('\n\t\t\tTabela de Pluviosidade')
    for i in range(ncidades):           # prcorrer as 3 cidades
        print('\n\t\t{:s}' .format(cidades[i]), end = '\t')

        for j in range(nmeses):         # percorrer os 6 meses
            print(rainfall[i][j], end = '\t')
        print('\n')


def dataAnalysis(rainfall):
    # Media de cada cidade 
    avgCidades = [0] * 3            # lista com 3 posições, media de cada cidade
    for i in range (ncidades):      # Percorre as 3 cidades
        avgCidades[i] = sum(rainfall[i])/len(rainfall[i])       # sublista i corresponde a uma cidade 
        print("Média de pluviosidade de {:s} = {:.2f}" .format(cidades[i], avgCidades[i]))
    
    print('\n\n')
    # Media de cada mês    
    sumMeses = [0] *6
    for j in range(nmeses):         # para cada mês de jan a jun
    #    sumMeses[j] = rainfall[0][j] +  rainfall[1][j] +  rainfall[][j]
        for i in range(ncidades):       # vamos iterar as 3 cidades
            sumMeses[j]+=  rainfall[i][j]
        print("Média do mês de {:s} = {:.2f}" .format(meses[j], sumMeses[j]/ncidades))
            

#--- EX02 - INPUT RAINFALL
rainfall = []
for i in range (ncidades):           # 3 cidades
    print('\n\t\t\tPluviosidade em {:s}' .format(cidades[i]))
    rainfall.append([])             # Adiciona uma nova linha (cidade)
    for j in range(nmeses):
        pluv = int(input('\t\t\t {:s}:' .format(meses[j])))
        rainfall[i].append(pluv)    # append do input na sublista i
    print('\n')

showData(rainfall)
dataAnalysis(rainfall)