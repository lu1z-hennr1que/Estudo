'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
'''
def compra_(quilo, fruta):
    if fruta == 'morango' or fruta == 'Morango':
        if quilo <= 5:
            pagar = quilo*2.5
            return pagar
        else:
            pagar = quilo*2.2
            return pagar
    elif fruta == 'maça' or fruta == 'Maça':
        if quilo <= 5:
            pagar = quilo*1.8
            return pagar
        else:
            pagar = quilo*1.5
            return pagar
    else:
        return False
def desconto_(compra, quilo):
    if compra >= 25 or quilo >= 8:
        desc_ = compra - (compra*0.1)
        compra = compra*0.1
        return desc_, compra

print('===============  TABELA DE  PREÇOS  ==================')
print('                      Até 5 Kg           Acima de 5 Kg')
print('Morango         R$ 2,50 por Kg          R$ 2,20 por Kg')
print('Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg')
print('')

fruta = input('Digite qual furta vai querer: ')
quilo = float(input('Digite quantos quilos vai querer: '))
comp = compra_(quilo, fruta)
resta, desconto = desconto_(comp, quilo)

print('=======================================================')
print('valor total da compra: ', comp, 'R$')
print(f'Valor do desconto: {desconto}R$')
print('Valor a pagar: ', resta, 'R$')

