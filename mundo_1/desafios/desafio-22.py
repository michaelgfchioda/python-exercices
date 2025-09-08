# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')) #.strip()
# Eu poderia colocar .strip() no final para o nome já entrar sem considerar os espaços
print('\nAnalisando seu nome...')
# Nome completo para maiúsculo
print('O seu nome completo maiúsculo é {}'.format(nome.upper()))
# Nome completo para minúsculo
print('O seu nome completo minúsculo é {}'.format(nome.lower()))
# Quantos caracteres (sem contar os espaços)
print('O total de caracteres sem os espaços é {}'.format(len(nome) - nome.count(' ')))
# Quantos caracteres têm o primeiro nome
nome = nome.split()
print('O total de caracteres do primeiro nome ({}) é {}'.format(nome[0], len(nome[0])))

"""nome = str(input('Digite seu nome completo: ')).strip()
print('\nAnalisando seu nome...')
print('Seu nome completo em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome completo em letras minúsculas é {}'.format(nome.lower()))
# Total de letras sem os espaços
print('O total de caracteres sem os espaços é {}'.format(len(nome) - nome.count(' '))) # Eu posso, simplesmente, pedir 
# o comprimento da string e "subtrair" o/os espaço(s) entre os nomes usando len(nome) - nome.count(' ')
# Total de letras no primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # Dessa forma, eu consigo encontrar o primeiro nome,
# pois ele ocupa o primeiro mini espaço da string"""
