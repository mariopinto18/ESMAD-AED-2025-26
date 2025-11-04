import math

# recebe uma lista de numeros e devolve quantos são superiores à media
def dataGrades(listNotas):
    """
    receives a list of grades and
    returns the highest, the lowest grades and how many grades are above average\n
    Args: listGrades - list of float numbers
    """
    media = sum(listNotas)/ len(listNotas)
    print(media)
    cont=0
    for i in range (len(listNotas)):
          if listNotas[i] > media:
                cont+=1
    return max(listNotas), min(listNotas), cont


# EX01
listNotas = []
i=1
while i<=10:          # ler 10 numeros e adicinar à lista
        try:
            numero =float(input("{} ª avaliação:" .format(i)))
            if numero <0 or numero >20:
              raise ValueError
            listNotas.append(numero)
            i+=1
        except ValueError:
                print("Deve inserir uma avaliação emtre [0-20]")
        except:
              print("Valor inválido. Tente novamente!")
maior, menor, cont = dataGrades(listNotas)
print("\n", listNotas)
print("\n\nMaior nota  {:.2f} \n\nMenor nota: {:.2f}, \n\nNº notas acima média= {:n}" .format(maior, menor, cont))


