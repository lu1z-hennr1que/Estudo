# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
# multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do
# programa com as mensagens adequadas.

Peso_peixe = int(input('Digite os quilos de peixe:'))

if Peso_peixe > 50:
    peso_multa = (Peso_peixe-50)*4
    print(f'A quantidade dos quilos de peixe passou do limite estabelecido pelo regulamento de pesca do estado de São paulo.\nVai pagar uma multa de {peso_multa:.2f} R$ pelo peso de peixes ter passado dos 50kg.')
else:
    print('Parabéns, seu peso deu a baixo de 50 quilos, não vai precisar pagar muita!')