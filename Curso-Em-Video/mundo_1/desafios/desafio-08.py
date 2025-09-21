# 8. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

ms = float(input('Quantos metros? '))
km = ms / 1000
hm = ms / 100
dam = ms / 10
dm = ms * 10
cm = ms * 100
mm = ms * 1000
print('\nConvertendo a medida de {}ms, teremos:'.format(ms))
print('Em quilômetros:  {}km'.format(km))
print('Em hectômetros:  {}hm'.format(hm))
print('Em decâmetros:   {}dam'.format(dam))
print('Em decímetros:   {:.0f}dm'.format(dm))
print('Em centímetros:  {:.0f}cm'.format(cm))
print('Em milímetros:   {:.0f}mm'.format(mm))
