'''
O Hipermercado Tabajara está com uma promoção de carnes que é
imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar
apenas um dos tipos de carne da promoção, porém não há limites
para a quantidade de carne por cliente. Se compra for feita no
cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
o total da compra. Escreva um programa que peça o tipo e a
quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.

'''
def carne (tipo, quilo):
    try:
        if tipo == 'file duplo':
            if quilo <= 5:
                valor = quilo*4.90
                return valor
            else:
                valor = quilo*5.80
                return valor
        elif tipo == 'alcatra':
            if quilo <= 5:
                valor = quilo*5.90
                return valor
            else:
                valor = quilo*6.80
                return valor
        elif tipo == 'picanha':
            if quilo <= 5:
                valor = quilo*6.90
                return valor
            else:
                valor = quilo*7.80
                return valor
        else:
            print('Error no programa!')
    except:
        print('Error no calculo!')

def pagamento (pag):
    try:
        if pag == 'cartão tabajara' or pag == 'cartão da loja' or pag == 'o cartão taajera':
            pag_ = 'cartão'
            return pag_
        elif pag == 'reais' or pag == 'em reais' or pag == 'em nota':
            pag_ = 'Reais'
            return pag_
        elif pag == 'a vista' or pag == 'no crédito' or pag == 'no cartão':
            cartão = input('mas qual cartão mano? ')
            print('Beleza, mano...')
            pag_ = cartão
            return pagamento(pag_)
    except:
        print('Deu erro no programa')
        return pag

tipo_carne = input('As carnes que temos hoje:\n\n- File duplo \n- Alcatra \n- Picanha\n\nQual tipo de carne vai levar hoje chefe? ')
if tipo_carne == 'file duplo' or tipo_carne == 'alcatra' or tipo_carne == 'picanha':
    quant_carne = float(input('\nVai levar quantos quilos em? '))
    pag = input('\nCara, Se compra for feita no cartão Tabajara o cliente receberá ainda um '
            'desconto de 5% sobre o total da compra.\nQual é a forma de pagamento mano? ')
else:
    print('Digita um valor valido cara, não isso!... Programa encerrado!')

preco_total = carne(tipo_carne, quant_carne)
pagam = pagamento(pag)
liquido = 0.0
desc = 0.0

if pagam == 'cartão':
    desc = preco_total * 0.05
    liquido = preco_total - desc
elif pagam == 'reais':
    liquido = preco_total
    desc = 0.00
print('')
print('############## CUPOM FISCAL ###############')
print('')
print(f'Tipo de carne      : {tipo_carne}')
print(f'Quantidade de carne: {quant_carne} Kg')
print(f'Preço total        : {preco_total} R$')
print(f'Tipo de pagamento  : {pagam}')
print(f'Valor de desconto  : {desc:.2f} R$')
print(f'Valor a pagar      : {liquido:.2f} R$')
print('')
print('########## OBRIGADO PELA COMPRA ###########')