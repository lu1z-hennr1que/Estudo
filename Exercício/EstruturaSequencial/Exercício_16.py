# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
# quantidades de latas de tinta a serem compradas e o preço total.

metro_area = float(input('Digite a quantidade de metros quadrados da área a ser pintada: '))
litro_area1 = metro_area/3
if litro_area1 <= 18:
    print(f'Vai precisar apenas de 1 lata.\nPreço total: R$ 80,00.')
else:
    litro_area2 = litro_area1*4.44444444444
    print(f"Vai precisar de {litro_area1:.2f} litros.\nValor total: {litro_area2:.2f}")