# 6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = float(input('Digite um número: '))
print('\nO dobro desse número é {}'.format(num * 2))
print('O triplo desse número é {}'.format(num * 3))
print('A raiz quadrada desse número é {:.2f}'.format(num**(1/2))) # ou pow(num,(1/2))
# Eu poderia ter atribuído à duas novas variáveis o dobro, triplo e a raiz quadrada, também,
# o que seria o ideal se eu precisasse utilizar o resultado de cada uma mais pra frente no programa.
