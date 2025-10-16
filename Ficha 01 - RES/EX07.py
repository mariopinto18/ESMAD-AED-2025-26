""" 
simulator should print the FCM (Frequência Cardiaca Máxima | Maximum Heart Rate)
based on gender and age, such as: 
• feminine gender: FCM = 226 - age bpm (heartbeats per minute)
• masculine gender: FCM = 220 - age bpm (heartbeats per minute) 
"""

validGender = ['M', 'm', 'F', 'f']

gender = input("\n\n\nGender(M/F): ")
if gender not in validGender:   # valida se gender está na lista validGender
    print("\nIncorret gender")
    exit()

idade = int(input("\nAge: "))
match gender.upper():           # upper - converte para maiúsculas
    case "F":
        indiceFCM = 226- idade
    case "M":
        indiceFCM = 220- idade
    case _:
        print("Incorret gender!")
        exit()

print(f'\nFCM= {indiceFCM} bpm' )



