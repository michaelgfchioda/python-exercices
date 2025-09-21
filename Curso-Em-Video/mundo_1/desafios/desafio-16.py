# 16. Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

# Fazendo o exercício importando toda a biblioteca matemática
"""import math
num = float(input('Digite um número real qualquer: '))
print('O número {} tem sua porção inteira {}'.format(num, math.trunc(num)))"""

# Fazendo o exercício importando somente a funcionalidade trunc() de math
'''from math import trunc
num = float(input('Digite um número real qualquer: '))
print('O número {} tem sua porção inteira {}'.format(num, trunc(num)))'''

# É possível fazer esse exercício sem importar o módulo math, também, deixando a variável inteira no print()
'''num = float(input('Digite um número real qualquer: '))
print('O número {} tem sua porção inteira {}'.format(num, int(num)))'''

# Também é possível editando somente a máscara{} do print()
'''num = float(input('Digite um número real qualquer: '))
print('O número {} tem sua porção inteira {:.0f}'.format(num, num))'''
