# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
valor_hora, dia_traba, hora_traba = float(input('Digite quanto você ganha por hora: ')), int(input('Digite quantas horas trabalha por dias:')), int(input('Digite quantos dias você trabalhou no mês: '))
salario_bru = (valor_hora*hora_traba*dia_traba)
ir = salario_bru*0.11
inss = salario_bru*0.08
sindicato = salario_bru*0.05
salario_liq = salario_bru-(ir+inss+sindicato)
print(f'+ Salário Bruto   : {salario_bru:.2f} R$')
print(f'- IR (11%)        : {ir:.2f} R$')
print(f'- INSS (8%)       : {inss:.2f} R$')
print(f'- Sindicato ( 5%) : {sindicato:.2f} R$')
print(f'= Salário Liquido : {salario_liq:.2f} R$')