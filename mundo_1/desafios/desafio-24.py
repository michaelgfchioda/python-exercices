# 24. Crie um programa que digite o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].title() == 'Santo') # Dessa forma é mais eficiente, pois independente da forma que o usuário escrever
# o nome da cidade, ele será transformado no .title() e dará certo
# print('Santo' in cidade[0:5])
