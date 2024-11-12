# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

Valor_hora = float(input('Digite quanto você ganha por hora:'))
Hora_trabalhada = float(input('Digite o número de horas trabalhadas no mês:'))
Salario_mes = Valor_hora * Hora_trabalhada
print(f"Total do seu salário esse mês é {Salario_mes:.2f}")
