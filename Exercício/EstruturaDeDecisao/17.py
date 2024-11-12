'''Faça um Programa que peça um número correspondente a um determinado 
ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input('Digite o ano: '))
valores = ano%100
if valores == 00:
    if ano%400 == 0:
        print('É bissesto.')
    else:
        print('Não é bissexto.')
else:
    if valores%4 == 0:
        print('É bissexto.')
    else:
        print('Não é bissexto.')