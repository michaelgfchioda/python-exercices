# 13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o seu salário? R$'))
aumento = salario + (salario * (15/100))
print('Com 15% de aumento, você vai receber R${:.2f}'.format(aumento))
