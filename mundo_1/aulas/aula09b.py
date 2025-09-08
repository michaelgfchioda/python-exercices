"""ANÁLISE DE STRINGS"""

frase = 'Curso em Vídeo Python'
'''
print(len(frase)) - "len" vem de lenf(comprimento). A função len() serve para mostrar o tamanho da string.

print(frase.count('o')) - A função cont() serve para contar quantas letras específicas há na string, tipo "o" minúsculo.

print(frase.count('o', 9, 21)) - A função count('o', 9, 21) serve para contar quantas letras "o" minúsculas existem 
entre os índices 9 e 21.

print(frase.find('Python')) - A função .find() serve para encontrar uma sequência específica de caracteres, mostrando o
índice que essa sequência começa.

print(frase.find('Android')) - Quando se utiliza a função .find() para encontrar uma palavra que não existe na string
analisada, o programa retornará "-1", indicando que não existe.

print('Curso' in frase) - Essa é uma forma de saber se existe ou não uma palavra específica dentro de uma string.
Se existir, o programa retornará "True" para confirmar que sim, senão, o programa retornará "False", dizendo que não.
'''
