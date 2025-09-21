# 17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa

# Calculando utilizando a função hypot() para cálculo da hipotenusa
"""import math"""
from math import hypot
print('Digite o comprimento dos catetos para encontrar a hipotenusa')
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjcente = float(input('Cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjcente)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))

# Calculando utilizando toda a biblioteca math
'''import math
print("Digite o comprimento dos catetos para encontrar a hipotenusa")
cateto_adj = float(input('Cateto adjacente: '))
cateto_ops = float(input('Cateto oposto: '))
hipotenusa = math.sqrt(math.pow(cateto_adj, 2) + math.pow(cateto_ops, 2))
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''

# Calculando utilizando somente sqrt() e pow()
'''from math import sqrt, pow
print("Digite o comprimento dos catetos para encontrar a hipotenusa")
cateto_adj = float(input('Cateto adjacente: '))
cateto_ops = float(input('Cateto oposto: '))
hipotenusa = sqrt(pow(cateto_adj, 2) + pow(cateto_ops, 2))
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''

# Calculando sem utilizar a biblioteca math
'''print('Digite o comprimento dos catetos para encontrar a hipotenusa')
cateto_adj = float(input('Cateto adjacente: '))
cateto_ops = float(input('Cateto oposto: '))
hipotenusa = ((cateto_adj ** 2) + (cateto_ops ** 2)) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''
