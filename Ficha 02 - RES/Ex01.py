""" 
factorial of a number
"""

numero = int(input("Enter a number: "))

if numero <0:
    print("The number should be >=0")
    exit()

# it's a positivo number >=0
fatorial=1                          # inicializa fatorial a 1
for i in range(numero, 1, -1):      # repete do numero lido até 1 (decrescente)
    fatorial*=i

#print(f'Fatorial de {numero} = {fatorial}')
print('Fatorial de {:n} = {:n}' .format(numero, fatorial))
