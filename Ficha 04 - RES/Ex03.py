
"""
Create a program that allows you to generate a random number between [1-100] and display it in the Console. 
"""
import random

limInf=1            
limSup = 100
listNumbers = []
opcao = ""
while opcao != "N":
    number = random.randint(limInf, limSup) # gerar aleatótio entre +ultimo gerado e 100
    listNumbers.append(number)
    print("\n\t\t\t Numero sorteado: ", number)
    if number== 100:        # quando é gerado o nº 100, termina
        break
    limInf= number+1        # LimInf é sempre o último gerado + 1
    opcao = input ("Quer gerar um novo número? (S/N)? ").upper()

listNumbers.sort(reverse=True)
print(listNumbers)

