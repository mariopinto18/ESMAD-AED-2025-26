"""
Prints the first n terms of the Fibonacci sequence, 
where the number of desired terms (n) must be indicated by user
"""
nTermos = int(input("\n\n\n\t\t\t Nº of termos a imprimir:"))
if nTermos < 1:
    print("O nº de termos a imprimir da sequencia de Fibonacci deve ter pelo menos 1!")
    exit()

resutTermos= ""
# Tratamos os 2 primeiros termos, casos particulares
if nTermos >= 1:        # trata 1º termo da sequencia
    resultTermos = "0"

if nTermos >= 2:        # trata 2º termo da sequencia
    resultTermos+= ", 1"

penultimoTermo = 0
ultimoTermo = 1

# Tratamos os termos seguintes - do 3º em diante
for i in range(3, nTermos+1):                    # para todos a partir do 3º termo
    novoTermo = penultimoTermo + ultimoTermo     # cada termo resulta da soma dos 2 anteriores
    resultTermos+= ", " + str(novoTermo)         # vai contactar os termos numa variavel de texto
                                                 # para facilitar a impressão do resultado
    penultimoTermo = ultimoTermo
    ultimoTermo = novoTermo

print(f'\n\n\t\t\t Primeiros {nTermos} termos da sequência de Fibonacci: {resultTermos}')


