""" 
reads a number (integer and positive) and indicates
whether it is a prime number or not
"""

numero = int(input("Indique um número:"))
if numero <=1:
    print("O número a indicar deve ser superior a 1")
    exit()
primo = True
for i in range(2, numero):      # o divisor varia entre 2 e o numero-1
    if numero % i == 0:         # quando encontro um resto 0 => não é primo
        primo = False           # logo, variável primo = False
        break

if primo == True:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} NÃO é primo')


