"""
Develop a program that simulates the game of guessing a number.
The program should start by generating a random number (between 1 and
50), allowing the player to iteratively try to guess the number generated
by the computer
"""
import random    # random / numeros aleatórios 
print("\t\t Guess the Number Game!\n")
print("\t\t-------------------------\n")

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

