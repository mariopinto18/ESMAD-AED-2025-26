"""
Write a program that implements an Ideal Weight Simulator (version 2.0!). 
The algorithm should ask the user for their gender (M for male and F for female)
and height (in cm). 
The simulation of ideal weight (Peso Ideal) is given by the following 
formula: Ideal weight = (h-100) - (h-150)/k Whereas: k = 2 for females and k = 4 for males
h is the height in cm 
"""

gender = input("Enter the gender (M/F): ").lower()   # minusculas
if gender != "m" and gender != "f":
    print("Incorret data of gender!")
    exit()
height = int(input("Enter the height (cm): "))

if gender == 'f': 
    k=2 
else: 
    k=4

idealWeight = (height- 100) - (height - 150) / k
print("O Peso Ideal é {:.2f} Kg" .format(idealWeight))
print("\n")
