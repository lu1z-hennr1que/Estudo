'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O
programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.

No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''
def desconto_do_IR(salario):
    if salario > 900 and salario <= 1500:
        desconto_ir = salario * 0.05
        porcentagem = '5%'
        return desconto_ir, porcentagem
    elif salario > 1500 and salario <= 2500:
        desconto_ir = salario * 0.1
        porcentagem = '10%'
        return desconto_ir, porcentagem
    elif salario > 2500:
        desconto_ir = salario * 0.2
        porcentagem = '20%'
        return desconto_ir, porcentagem
    else:
        desconto_ir = 'isento'
        porcentagem = '0'
        return desconto_ir, porcentagem
valor_hora = float(input('Digite o valor da sua hora de trabalho? '))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês? "))
salario = valor_hora * horas_trabalhadas
desconto_ir, porcentagem = desconto_do_IR(salario)
inss = (salario*0.1)
fgts = (salario*0.11)
if desconto_ir == int:
    liquido = salario - (porcentagem + inss + fgts)
else:
    liquido = salario - (inss + fgts)
print('')
print(f'Salário Bruto:            :{salario}')
print(f'(-) IR ({porcentagem})               :{desconto_ir}')
print(f'(-) INSS (10%)            :{inss}')
print(f'FGTS (11%)                :{fgts}')
print(f'Total de descontos        :{liquido}')