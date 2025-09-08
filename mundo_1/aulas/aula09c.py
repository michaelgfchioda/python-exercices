"""TRANSFORMAÇÃO DE STRINGS"""

frase = 'Curso em Vídeo Python'
frase2 = '   Curso em Vídeo Python   '
'''
print(frase.replace('Python', 'Ótimo')) - Usando o método .replace(), é possível trocar uma palavra existente na string
por outra, sendo, primeiro, dentro do parênteses e entre aspas simples ou duplas, a que existe na string e depois da 
vírgula, a que vai entrar no seu lugar. 
Dessa forma: frase = frase.replace('Python', 'Ótimo')

print(frase.upper()) - Ao usar o método .upper(), é possível deixar todas as letras da string maiúsculas.

print(frase.lower()) - Ao usar o método .lower(), é possível deixar todas as letras da string minúsculas.

print(frase.capitalize()) - Usando o método .capitalize(), todas as letras da string ficarão minúsculas, 
exeto a primeira, localizada no índice "0" da string.

print(frase.title()) - Usando o método .title(), todas as palavras da string ficarão com somente a primeira 
letra maiúscula.

print(frase2.strip()) - Usando o método .strip(), é possível eliminar todos os espaços inúteis antes da primeira palavra
e depois da última.
 
print(frase2.rstrip()) - Usando o método .rstrip(), é possível eliminar somente os espaços inúteis depois da última
palavra da string (r = right = direita).

print(frase2.lstrip()) - Usando o método .lstrip(), é possível eliminar somente os espaços inúteis antes da primeira
palavra da string.
'''
