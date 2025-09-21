# 19. Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

# Para fazer esse exercício, foi necessário utilizar uma "lista" para armazenar os nomes dos alunos entre [],
# e usar a função "choice()" da biblioteca "random" para sortear um nome e imprimir na tela
"""import random
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo: '))
nome3 = str(input('Nome do terceiro: '))
nome4 = str(input('Nome do quarto: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O escolhido foi o/a {}!'.format(escolhido))"""

from random import choice
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo: '))
nome3 = str(input('Nome do terceiro: '))
nome4 = str(input('Nome do quarto: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O escolhido foi o/a {}!'.format(escolhido))
