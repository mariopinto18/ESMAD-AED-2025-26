"""
VERSION 2.0. Asks if do you want to start a NEW GAME
"""
import random    # random / numeros aleatórios 
import os        # Library Operating System
print("\t\t Guess the Number Game!\n")
print("\t\t-------------------------\n")

resposta = "S"
while resposta != "N":
    os.system('cls')    # cls = clear screen
    numero = random.randint(1,50)  # random between  [1- 50]
    tentativas = 1
    palpite = int(input("Enter your {:n}º guess: " .format(tentativas)))

    while numero != palpite and tentativas <10:    # limit to 10 attempts
        if palpite > numero:
            print("The number is SMALLER \n")
        elif palpite < numero:
            print("The number is BIGGER \n")
        tentativas+= 1
        palpite = int(input("Enter your {:n}º guess: " .format(tentativas)))

    # Sai do ciclo while - ou porque acertou ou porque esgotou as 10 tentativas!
    if numero == palpite:
        print("Congratulations! You guessed the number in {:n} attempts!" .format(tentativas))
    else:
        print("You have used all the 10 attempts :( ")
    # end of game
    # Asks if restart a New Game
    resposta = input("NEW GAME(Y/N)?: ").upper()