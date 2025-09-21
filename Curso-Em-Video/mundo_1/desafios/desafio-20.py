# 20. O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# Para fazer o sorteio da ordem de apresentação de trabalhos desse exercício,
# é necessário realizar um sorteio que ninguém fique de fora, ou seja,
# uma ordem de apresentação, que mostre o nome de todos os alunos de forma embaralhada,
# não exatamente igual a entrada dos nomes(pode acontecer, claro, é aleatório!), então,
# foi preciso usar a função "shuffle()" da biblioteca "random" para misturar essas strings e imprimir
"""import random
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo: '))
nome3 = str(input('Nome do terceiro: '))
nome4 = str(input('Nome do quarto: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(lista)"""

# importação específica da função "shuffle()" ao programa
from random import shuffle
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('\nA ordem de apresentação será:')
print(lista)
