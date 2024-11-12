'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
 - o salário antes do reajuste;
 - o percentual de aumento aplicado;
 - o valor do aumento;
 - o novo salário, após o aumento.'''
def Reajuste_salarial(salario):
    if salario <= 280:
        reajuste = salario * 0.2
        percentual = '20%'
        return reajuste, percentual
    elif salario > 280 or salario <= 700:
        reajuste = salario * 0.15
        percentual = '15%'
        return reajuste, percentual
    elif salario > 700 or salario <= 1500:
        reajuste = salario * 0.1
        percentual = '10%'
        return reajuste, percentual
    elif salario > 1500:
        reajuste = salario * 0.05
        percentual = '5%'
        return reajuste, percentual
    else:
        print('Error no programa!')
salario = float(input('Digite o seu salário: '))
reajuste_salario, percentual = Reajuste_salarial(salario)
print('')
print('Salário antes do reajuste: ', salario)
print('Percentual de aumento aplicado: ', percentual)
print('Valor do aumento: ', reajuste_salario)
print('Novo salário, após o aumento: ', (salario + reajuste_salario))