"""DIVISÃO DE STRINGS"""

frase = 'Curso em Vídeo Python'
'''
print(frase.split()) - Ao usar a função .split(), a string se dividirá em uma lista, contendo cada palavra separadamente
como novas strings (todas elas partindo do índice "0"). Para acessar cada string da lista que será formada, basta
atribuir a uma nova variável ou a mesma, a função usada:
frase = frase.split()
print(frase[0]) - Para imprimir "Curso"
print(frase[4]) - Para imprimir "Python"
print(frase[4][1] - Para imprimir a letra "y" no índice 1 da string

'''

'''JUNÇÃO DE STRINGS'''

'''
print('-'.join(frase.split())) ou print(' '.join(frase)) - Essa função é responsável por pegar uma lista de strings e
junta-las, transformando-as em uma única string, substituindo o "espaço" entre elas por um caracter qualquer entre as 
aspas ou deixando um espaço vazio para manter o "espaço" se prefirir.
print('-'.join(frase).split()) - Primeiro os "espaços" são substituídos por "-" e depois é divida em uma lista, sendo 
cada palavra uma nova string.
'''
