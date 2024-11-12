# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
# litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# ° comprar apenas latas de 18 litros;
# ° comprar apenas galões de 3,6 litros;
# ° misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
area = int(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
litro = area/6

if litro < 3.6:
    print(f'vai precisar de {litro:.3f} litros')
    print(f'Comprar apenas um galão de 3,6 litros\n Valor total R$ 25.00')
elif litro < 18:
    print(f'vai precisar de {litro:.3f} litros')
    galao = litro/3.6
    print(f'Comprar apenas {round(galao+0.5)} galões de 3,6 litros')
    print(f'Valor total R$ {round(galao+0.5)*25:.2f}')
else:
    print(f'vai precisar de {litro:.3f} litros')
    lata = litro/18
    if (lata-int(lata)) < 1:
        galao = (lata-int(lata))*18/3.6
        print(f'Comprar {round(galao+0.5)} galões de 3,6 litros')
    galao = (lata - int(lata)) * 18 / 3.6
    print(f'Comprar {round(lata-0.5)} latas de 18 litros')
    print(f'Valor total R$ {(round(lata-0.5)*80)+round(galao+0.5)*25:.2f}')
