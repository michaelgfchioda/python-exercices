# 27. Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhcer, {}!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
# Uma lista é formada com cada nome separadamente. Para mostrar o último nome, você precisa usar o len(nome) entre
# colchetes e substrair 1 (-1) para imprimir o último nome
