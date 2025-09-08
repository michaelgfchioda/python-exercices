# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Qual o valor do produto? R$'))
desconto = produto - (produto * (5/100))
print('O novo valor desse produto, com o desconto de 5%, será R${:.2f}'.format(desconto))
