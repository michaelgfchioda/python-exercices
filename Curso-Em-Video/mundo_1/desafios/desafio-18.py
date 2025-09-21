# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

# Para calcular o seno, cosseno e tangente, foi necessário utilizar as funcionalidades:
# math.sin() - SENO
# math.cos() - COSSENO
# math.tan() - TANGENTE
# Essas funcionalidades trabalham com graus radianos, ou seja,
# é preciso fazer a conversão para radianos utilizando: math.radians()
"""import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O Seno é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}'.format(seno, cosseno, tangente))"""

from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {}° possui:'.format(angulo))
print('SENO igual a {:.2f}'.format(seno))
print('COSSENO igual a {:.2f}'.format(cosseno))
print('TANGENTE igual a {:.2f}'.format(tangente))
