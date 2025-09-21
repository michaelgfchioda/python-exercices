# 7. Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nome = str(input('Qual o seu nome? '))
print('Olá, {}! Digite suas notas: '.format(nome))
nota1 = float(input('\nPrimeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('\n{}, sua média é {:.2f}'.format(nome, media))
# Ao invés de usar uma variável para atribuir à média, eu poderia ter feito o cálculo no print(), dessa forma:
# print('\n{}, sua média é {:.2f}'.format(nome, (nota1 + nota2)/2))
