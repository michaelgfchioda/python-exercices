# 25. Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome completo: ')).strip() #.title()
print('Você tem Silva no nome? {}'.format('Silva' in nome.title()))
# print('Silva' in nome)
