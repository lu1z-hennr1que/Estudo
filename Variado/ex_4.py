salar1o = float(input("Digite seu salário total:"))
ir = salar1o*0.11
inss = salar1o*0.08
sind = salar1o*0.05
total = ir+inss+sind
salario = salar1o-total
print("(+) Salário Bruto:   R$", salar1o)
print("(-) IR (11%):        R$", ir)
print("(-) INSS (8%):       R$", inss)
print("(-) Sindicato (5%):  R$", sind)
print("(-) Total Desconto:  R$", total)
print("(=) Salário Liquido: R$", salario)