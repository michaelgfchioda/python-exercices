# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos? '))
paycar = dias * 60
paykm = km * 0.15
valor_total = paycar + paykm
print('\nVocê alugou o carro por {} dias e percorreu {:.2f}km, então,\no valor total a pagar é R${:.2f}'.format(dias, km, valor_total))
