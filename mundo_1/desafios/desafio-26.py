# 26. Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()
print('A quantidade de letra A na frase é {}'.format(frase.count('A')))
print('A letra A aparece pela primeira vez no índice {}'.format(frase.find('A')))
print('A letra A aparece pela última vez no índice {}'.format(frase.rfind('A')))
# Se eu escrever +1 ao lado de .find() (frase.find()+1, ao invés de imprimir o índice 0, ele vai imprimir 1
