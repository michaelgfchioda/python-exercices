# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Qual a temperatura em °C? '))
fahrenheit = ((9 * celsius)/5) + 32
# Não é necessário usar os parênteses nesse caso,
# pois seguindo a ordem de precedência,
# os cálculos serão feitos da forma correta,
# começando pelo que vem primeiro: 9 * celsius / 5 + 32
# Fórmula de conversão de temperatura de Celsius para Fahrenheit
print('Convertendo a temperatura {:.0f}°C para Fahrenheit, a temperatura é {:.0f}°F'.format(celsius, fahrenheit))
