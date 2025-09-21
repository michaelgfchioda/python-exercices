# 10. Crie um programa que leia quanto dinheiro a pessoa tem na sua carteira e mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem? R$'))
print('Você pode comprar U${:.2f}!'.format(real / 3.27))
# Valor do dólar no dia 07/07/2024 em reais é R$5.46

# Ao invés de colocar o cálculo no format(), você pode criar outra variável para receber esse valor e usá-la no print()
