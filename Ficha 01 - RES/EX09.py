"""
IMC simulator
After calculating and printing the IMC, the program should categorize the individual,
based on the IMC index obtained
"""

weight = float(input("Entre your weight (kg):"))
height = float(input("\nEnter your height(m):"))

#Calcula e imprime o índice de massa corporal, IMC
indiceImc = weight/(pow(height,2))        # função pow(base, expoente)

print('\nYour IMC is: {:.2f}' .format(indiceImc))

# categoriza o indivíduo conforme o IMC obtido
if indiceImc < 18.5:
    print("\tlow weight ")
elif indiceImc < 25:
    print("\tnormal weight")
elif indiceImc < 30:
    print("\tover weight")
elif indiceImc < 35:
    print("\tGrade I obesity")
elif indiceImc <40:
    print("\tGrade II obesity)")
else:
    print("\tMorbyd obesity")


