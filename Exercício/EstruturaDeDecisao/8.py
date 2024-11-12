'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
'''
valor_produto = float(input('Digite o preço do produto: '))
valor_produto2 = float(input('Digite o preço do segundo produto: '))
valor_produto3 = float(input('Digite o preço do terceiro produto: '))
lista_de_valores = sorted([valor_produto, valor_produto2, valor_produto3])
print('Recomendo comprar o produto nesse valor: ', lista_de_valores[0], '$')