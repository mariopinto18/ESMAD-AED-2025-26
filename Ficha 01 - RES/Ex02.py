""" 
Ler um nome e um apelido, 
imprimindo no formatro Apelido, Nome
"""
nomeProprio = input("\nNome próprio: ")
nomeApelido = input("\nApelido:")

print('\n' + nomeApelido + ',', nomeProprio)

print("{:s}, {:s}" .format(nomeApelido, nomeProprio))
