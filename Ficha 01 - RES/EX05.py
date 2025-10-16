"""
Write a program that reads an integer and determines whether 
that number is even or odd (par ou ímpar)
"""

number = int(input("Indique um número: "))
if number %2 == 0:    # resto da divisão = 0 => é par
    print("O número {:n} é par" .format(number))
else:
    print("O número {:n} é ímpar" .format(number))
