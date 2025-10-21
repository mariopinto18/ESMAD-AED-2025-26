"""
checks if a given number (integer and positive) is a perfect number
"""

numero = int(input("Indique um número:"))
if numero <0:
    print("O número a indicar deve ser >=0")
    exit()

soma=0
for i in range(numero-1, 0, -1):
    if numero & i == 0:        # neste caso i é dividor do número
        soma+= i

print("\n")
if soma == numero:
    print("{0} é um número perfeito" .format(numero))
else:
    print("{0} NÃO é um número perfeito" .format(numero))
    