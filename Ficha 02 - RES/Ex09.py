""""
Read a set of n integers (where n is previously specified by the user).
Then determine the second largest value among the set of numbers read
"""

max1 = 0     # Maior numero 
max2 = 0     # segundo maior numero

n= int(input("How many numbers do you want to read? "))
i=0
while i < n:
    numero = int(input("Número:"))      # ler n numero
    i+=1
    if numero > max1:                   # Se numero lido é superior ao maior
          max2 = max1
          max1 = numero
    elif numero > max2:                 # Se numero lido é superior ao segundo maior
          max2 = numero

print(f'\n\n\t\tThe second biggest number is: {max2}' )
