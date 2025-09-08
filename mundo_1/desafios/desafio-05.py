# Faça um programa em python que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e
# todas as informações possíveis

n = input('Digite algo: ')
print('A variável é do tipo primitivo', type(n))
print('É numérico? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Só tem letra maiúscula? ', n.isupper())
print('Só tem letra minúscula? ', n.islower())
print('Só tem espaços? ', n.isspace())
print('É capitalizada? ', n.istitle())

# n = input('Digite algo: ')
# print('A variável é do tipo primitivo: ', type(n))
# print('É numérico? {}'.format(n.isnumeric()))
# print('É alfabético? {}'.format(n.isalpha()))
# print('É alfanumérico? {}'.format(n.isalnum()))
# print('Só tem letra maiúscula? {}'.format(n.isupper()))
# print('Só tem letra minúscula? {}'.format(n.islower()))
# print('Só tem espaços? {}'.format(n.isspace()))
# print('É capitalizada? {}'.format(n.istitle())

# n = input('Digite algo: ')
# if n.isalpha():
#    print('É alfabético!')
# elif n.isnumeric():
#    print('É numérico!')
# elif n.isalnum():
#    print('É alfabético e numérico!')
# else:
#    print('Não se enquadra em nenhuma categoria proposta')
