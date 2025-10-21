"""
calculates the sum of all pairs between that range 
(including the indicated limits).
"""

limiteInf =int(input("Lower number:"))
limiteSup =int(input("Upper number:"))

somaNumeros=0
for i in range(limiteInf, limiteSup+1):
    if i % 2 ==0:                 # pair number / número par
        somaNumeros+= i           # soma
        
print(f"The sum of all even numbers between {limiteInf} e {limiteSup} é {somaNumeros}")