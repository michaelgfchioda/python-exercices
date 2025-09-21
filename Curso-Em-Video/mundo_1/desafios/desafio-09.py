# 9. Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número: '))
print('A tabuada do número {} é:'.format(num))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num * 1))
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {:2} = {}'.format(num, 10, num * 10))
print('-' * 12)
# Eu poderia ter escrito o número como string ao invés de usar uma máscara assim {:2},
# mas eu não conseguiria alinhar os números da tabela da tabuada,
# porque, por exemplo, diferente dos números de 0 a 9,
# os números de 10 a 99, ocupam dois caracteres, então, dessa forma,
# é possível permitir que os números de 0 a 9 ocupem
# dois caracteres, também. Com isso, os números ficarão alinhados e bonitos visualmente,
# como pôde ver ao executar o programa.
