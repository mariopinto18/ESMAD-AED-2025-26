"""
 Reads a number (between 1 and 99) and determines
its representation in binary language.
"""

numero = int(input("Número: "))

result = ""                 # variavél que ira conter o resultado em binario
while (numero >1):
    resto = numero % 2      # encontar resto da divisão por 2
    result+= str(resto)     # Guardar no result o resto (0, 1)
    numero = int(numero / 2)

result+= str(numero)        # Guardar no result o resto (0, 1)
print(result[::-1])         # Inverte a ordem do resultado (string)











